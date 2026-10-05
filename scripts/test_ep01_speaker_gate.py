"""Synthetic behavior tests only. No test establishes real voice identity."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
import wave
from pathlib import Path
from ep01_speaker_gate import digest, fingerprint, evaluate


class SpeakerGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        def file(name, text):
            path = self.root / name
            path.write_text(text, encoding='utf-8')
            return {'path': str(path), 'sha256': digest(path)}
        self.file = file
        def audio_file(name):
            path = self.root / name
            with wave.open(str(path), 'wb') as audio:
                audio.setnchannels(1)
                audio.setsampwidth(2)
                audio.setframerate(8000)
                audio.writeframes(bytes(4 * 8000 * 2))
            return {'path': str(path), 'sha256': digest(path)}
        self.audio_file = audio_file
        self.voices = {'Đào': {'preset': 'D06', 'reference_id': 'dao-id'},
                       'Khoai': {'preset': 'K20', 'reference_id': 'khoai-id'}}
        lines = [{'id': 'N01', 'speaker': 'Đào', 'text': 'Câu của Đào.'},
                 {'id': 'N02', 'speaker': 'Khoai', 'text': 'Câu của Khoai.'}]
        package = file('package.json', json.dumps({'text_status': 'OWNER_APPROVED',
            'script_version': 'FIXTURE', 'voices': self.voices, 'lines': lines}, ensure_ascii=False))
        script = file('script.md', '\n'.join(f"**{r['id']} — {r['speaker']}:** “{r['text']}”" for r in lines))
        source = audio_file('source.wav')
        self.request = {'schema_version': 1, 'mode': 'AUDIO_SELECTION', 'package': package,
            'script': script, 'script_version': 'FIXTURE', 'target': None,
            'lines': [{'line_id': r['id'], 'text': r['text'], 'expected_speaker': r['speaker'],
                       'expected_voice': self.voices[r['speaker']], 'source': source,
                       'source_range': [i, i+1], 'timeline_range': [i+2, i+3],
                       'timing_basis': 'ASR_HINT_NOT_SAMPLE_ACCURATE'} for i, r in enumerate(lines)]}
        refs = {name: {'preset': v['preset'], 'reference_id': v['reference_id'],
            'audio': audio_file(name+'.wav'),
            'approval_evidence': file(name+'-approval.txt', 'SYNTHETIC APPROVAL'),
            'approved_reference_provenance_checked': True} for name, v in self.voices.items()}
        self.report = {'request_sha256': fingerprint(self.request), 'reviewer_id': 'fixture-critic',
            'maker_id': 'fixture-maker', 'independent_of_maker': True,
            'method': 'HUMAN_LISTENING_WITH_REFERENCE', 'actual_audio_reviewed': True,
            'references_compared': True, 'references': refs,
            'review_evidence': file('review.txt', 'SYNTHETIC ATTESTATION NOT REAL LISTENING'),
            'lines': [{'line_id': r['line_id'], 'heard_text': r['text'],
                'observed_speaker': r['expected_speaker'],
                'observed_voice_reference_id': r['expected_voice']['reference_id'],
                'identity_verdict': 'PASS', 'reviewed_full_source': True,
                'within_turn_identity_verdict': 'PASS_CONSISTENT', 'overlap_verdict': 'PASS_NO_OVERLAP',
                'observation': 'Synthetic fixture observation.'} for r in self.request['lines']]}

    def tearDown(self):
        self.temp.cleanup()

    def status(self):
        return evaluate(self.request, self.report)['status']

    def test_valid_fixture_source_scope_only(self):
        result = evaluate(self.request, self.report)
        self.assertEqual(result['status'], 'PASS')
        self.assertFalse(result['identity_detection_performed_by_gate'])
        self.assertFalse(result['release_authorized'])

    def test_missing_review_holds(self):
        self.assertEqual(evaluate(self.request, None)['status'], 'HOLD_FOR_INPUT')

    def test_boolean_schema_is_invalid(self):
        self.request['schema_version'] = True
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_malformed_package_holds(self):
        self.request['package'] = self.file('malformed-package.json', '[]')
        self.report['request_sha256'] = fingerprint(self.request)
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_asr_method_holds(self):
        self.report['method'] = 'ASR_ONLY'
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_anonymous_diarization_holds(self):
        self.report['method'] = 'ANONYMOUS_DIARIZATION'
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_no_actual_audio_holds(self):
        self.report['actual_audio_reviewed'] = False
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_string_boolean_holds(self):
        self.report['actual_audio_reviewed'] = 'true'
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_wrong_speaker_rework(self):
        self.report['lines'][0]['observed_speaker'] = 'Khoai'
        self.assertEqual(self.status(), 'REWORK')

    def test_wrong_voice_rework(self):
        self.report['lines'][0]['observed_voice_reference_id'] = 'other-id'
        self.assertEqual(self.status(), 'REWORK')

    def test_wrong_words_rework(self):
        self.report['lines'][0]['heard_text'] = 'Câu khác.'
        self.assertEqual(self.status(), 'REWORK')

    def test_voice_switch_within_turn_rework(self):
        self.report['lines'][1]['within_turn_identity_verdict'] = 'FAIL_SWITCHED'
        self.assertEqual(self.status(), 'REWORK')

    def test_overlap_rework(self):
        self.report['lines'][0]['overlap_verdict'] = 'FAIL_OVERLAP'
        self.assertEqual(self.status(), 'REWORK')

    def test_unchecked_within_turn_holds(self):
        self.report['lines'][1].pop('within_turn_identity_verdict')
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_unknown_speaker_holds(self):
        self.report['lines'][0]['observed_speaker'] = None
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_changed_source_hash_holds(self):
        Path(self.request['lines'][0]['source']['path']).write_text('CHANGED', encoding='utf-8')
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_changed_source_range_holds(self):
        self.request['lines'][0]['source_range'] = [0, 0.5]
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_changed_voice_reference_holds(self):
        self.report['references']['Đào']['reference_id'] = 'other-ref'
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_missing_reference_audio_holds(self):
        self.report['references']['Đào']['audio'] = None
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_same_maker_reviewer_holds(self):
        self.report['reviewer_id'] = self.report['maker_id']
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_missing_observation_holds(self):
        self.report['lines'].pop()
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_duplicate_observation_holds(self):
        self.report['lines'][1] = copy.deepcopy(self.report['lines'][0])
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_missing_listening_record_holds(self):
        self.report['review_evidence'] = None
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_invalid_time_holds(self):
        self.request['lines'][0]['source_range'] = [0, float('nan')]
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_source_interval_beyond_audio_holds(self):
        self.request['lines'][0]['source_range'] = [0, 5]
        self.report['request_sha256'] = fingerprint(self.request)
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_non_audio_reference_holds(self):
        self.report['references']['Đào']['audio'] = self.file('fake.wav', 'NOT WAV')
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_unheard_claim_is_unknown_not_confirmed_defect(self):
        self.report['actual_audio_reviewed'] = False
        self.report['lines'][0]['observed_speaker'] = 'Khoai'
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_unheard_line_does_not_confirm_defect(self):
        self.report['lines'][0]['reviewed_full_source'] = False
        self.report['lines'][0]['observed_speaker'] = 'Khoai'
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_changed_script_holds(self):
        Path(self.request['script']['path']).write_text('CHANGED', encoding='utf-8')
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def av_scope(self):
        self.request['mode'] = 'FINAL_AV'
        path = self.root / 'cut.mp4'
        ff = Path(__file__).resolve().parents[1] / '.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffmpeg.exe'
        if not ff.exists():
            self.skipTest('Verified FFmpeg required for synthetic AV fixture')
        subprocess.run([str(ff), '-nostdin', '-hide_banner', '-loglevel', 'error',
            '-f', 'lavfi', '-i', 'color=size=64x64:rate=1:duration=4',
            '-f', 'lavfi', '-i', 'anullsrc=r=8000:cl=mono', '-t', '4',
            '-c:v', 'libx264', '-c:a', 'aac', str(path)], check=True)
        self.request['target'] = {'path': str(path), 'sha256': digest(path)}
        self.report['request_sha256'] = fingerprint(self.request)

    def test_audio_pass_does_not_pass_final(self):
        self.av_scope()
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_wrong_visible_actor_rework(self):
        self.av_scope()
        self.report['actual_full_av_reviewed'] = True
        for row in self.report['lines']:
            row.update(sync_verdict='PASS_ONSCREEN', visible_speaker=row['observed_speaker'], other_character_silent=True)
        self.report['lines'][0]['visible_speaker'] = 'Khoai'
        self.assertEqual(self.status(), 'REWORK')

    def test_final_fixture_pass_with_full_review(self):
        self.av_scope()
        self.report['actual_full_av_reviewed'] = True
        for row in self.report['lines']:
            row.update(sync_verdict='PASS_ONSCREEN', visible_speaker=row['observed_speaker'], other_character_silent=True)
        self.assertEqual(self.status(), 'PASS')

    def test_changed_final_cut_holds(self):
        self.av_scope()
        Path(self.request['target']['path']).write_text('CHANGED', encoding='utf-8')
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_non_av_target_holds(self):
        self.av_scope()
        self.request['target'] = self.file('not-video.txt', 'NOT AV')
        self.report['request_sha256'] = fingerprint(self.request)
        self.report['actual_full_av_reviewed'] = True
        for row in self.report['lines']:
            row.update(sync_verdict='PASS_ONSCREEN', visible_speaker=row['observed_speaker'], other_character_silent=True)
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_audio_only_target_holds(self):
        self.av_scope()
        self.request['target'] = self.audio_file('audio-only.wav')
        self.report['request_sha256'] = fingerprint(self.request)
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_timeline_beyond_current_av_holds(self):
        self.av_scope()
        self.request['lines'][1]['timeline_range'] = [3, 5]
        self.report['request_sha256'] = fingerprint(self.request)
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_whitespace_does_not_hide_self_review(self):
        self.report['reviewer_id'] = ' ' + self.report['maker_id']
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_unapproved_offscreen_holds(self):
        self.av_scope()
        self.report['actual_full_av_reviewed'] = True
        for row in self.report['lines']:
            row.update(sync_verdict='PASS_APPROVED_OFFSCREEN')
        self.assertEqual(self.status(), 'HOLD_FOR_INPUT')

    def test_builder_requires_explicit_scope(self):
        script = Path(__file__).with_name('build_ep01_c_v06_assembly.py')
        result = subprocess.run([sys.executable, str(script), '--out', str(self.root/'never-render'),
            '--closing-asr', str(self.root/'missing.json')], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('--speaker-review', result.stderr)
        self.assertFalse((self.root/'never-render').exists())


if __name__ == '__main__':
    unittest.main()

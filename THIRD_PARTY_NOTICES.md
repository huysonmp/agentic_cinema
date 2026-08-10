# Third-party source notices

The repositories under `ext/` remain separate works checked out through Git submodules. Their own license and notice files govern those works; the Agentic Cinema Apache-2.0 license does not replace them.

| Path | Project | Pinned commit | Source | License identified upstream |
|---|---|---|---|---|
| `ext/generative-ai` | Google Cloud Generative AI | `db9c80f4ce3cf596d2e432aaab4dc3587e794dc2` | <https://github.com/GoogleCloudPlatform/generative-ai> | Apache License 2.0 |
| `ext/agent-starter-pack` | Agent Starter Pack | `659f047742457bd55e5db0edd088cf678b6f0669` | <https://github.com/GoogleCloudPlatform/agent-starter-pack> | Apache License 2.0 |
| `ext/adk-samples` | Agent Development Kit samples | `f9f7e2124b37426a104e54ec0ac93e83cdf3d9f5` | <https://github.com/google/adk-samples> | Apache License 2.0 |
| `ext/adk-python` | Agent Development Kit for Python | `0477e5743bdf5e0cce5a698951c7b70a07baa80a` | <https://github.com/google/adk-python> | Apache License 2.0 |
| `ext/python-genai` | Google Gen AI Python SDK | `66e224c39c9527e0fef3a4f049ac33ec941e2f99` | <https://github.com/googleapis/python-genai> | Apache License 2.0 |
| `ext/mcp-toolbox` | MCP Toolbox for Databases | `cf5a0c8fbf52f1e09fc565109682cf52b6ebd553` | <https://github.com/googleapis/mcp-toolbox> | Apache License 2.0 |
| `ext/modelcontextprotocol` | Model Context Protocol | `b25c0874bf0ba699a58e21ef06f659d839659de3` | <https://github.com/modelcontextprotocol/modelcontextprotocol> | Mixed during relicensing: Apache-2.0, MIT and CC-BY-4.0; read the pinned `LICENSE` |
| `ext/a2a` | Agent2Agent Protocol | `19598c4baddbbaf868595cf9f3119c89ec96329f` | <https://github.com/a2aproject/A2A> | Apache License 2.0 |

At the pinned MCP Toolbox commit, `.gitmodules` still declares `docs2/themes/godocs`, but no gitlink for that path is tracked, so it is not part of this recursive checkout. If a later pinned commit restores the gitlink, its license must be added to this inventory before accepting the update.

Before copying or modifying upstream material:

1. read the license and NOTICE files at the pinned commit;
2. retain required copyright, patent, trademark and attribution notices;
3. record the source path and pinned commit in the adapting change;
4. do not assume example datasets, media, model outputs or linked assets share the repository's code license.

This inventory is informational, not legal advice. `scripts/verify-submodules.ps1` verifies Git state, not license compliance.

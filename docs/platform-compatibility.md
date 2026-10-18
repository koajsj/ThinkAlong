# Platform Compatibility

Documentation checked: 2026-10-18. One core Skill and one portable-instructions fallback; no runtime dependencies or host integrations are added. The host decides discovery/loading and tool permissions; the model decides adherence. Actual result verification is a separate evidence layer. Matching metadata cannot guarantee any of these layers.

| Platform / host | Installation and selection | Execution boundary |
| --- | --- | --- |
| Codex | Install in `~/.agents/skills/think-along/` or project `.agents/skills/think-along/`. Natural requests can be matched against description; optional explicit `$think-along` remains available. | The existing default permits implicit selection; `policy.allow_implicit_invocation: true` states that policy explicitly. It neither forces selection nor grants workspace/shell access. |
| Claude Code | Install in `~/.claude/skills/think-along/` or project `.claude/skills/think-along/`. Claude can choose by description; optional `/think-along` invokes it explicitly. | The current session's repository access and permissions govern implementation. Codex-specific `openai.yaml` policy is not a cross-host activation control. |
| Claude web | Upload the single-root ZIP when custom Skills and code execution are enabled. | Cloud execution does not itself provide access to a local repository. Discuss normally; prepare a handoff only if implementation is requested and required access is missing. |
| ChatGPT web | Use the account/workspace's supported Skill installation controls; use portable instructions if unavailable. Selection and available tools depend on the surface and workspace. | Inspect the actual tools and accessible inputs. A web chat's execution or file tools do not automatically imply local project access. Do not assume every ChatGPT session is chat-only or can edit a repository. |
| DeepSeek or another model through a compatible host | Follow that host's Skill discovery and model configuration. See the DeepSeek Codex integration reference below. | Choosing a model does not install a Skill or grant tools. Host configuration and model adherence remain separate; no model-specific activation result is measured. |
| Plain chat without native Skills | Paste the relevant language from [portable instructions](../adapters/portable-instructions.md) into conversation or custom instructions. | This supplies guidance, not native discovery, tools, persistent memory or transfer between products. Continue within available context; consolidate a handoff only when necessary or requested. |

Folder installations must include the repository root `LICENSE` inside the installed `think-along/`; the generated ZIP includes it. Preserve the ZIP's single `think-along/` root, relative references and existing local edits on upgrades.

## Official references and review scope

- [OpenAI Skill creation, local directories and invocation policy](https://learn.chatgpt.com/docs/build-skills): natural matching and explicit selection are supported mechanisms, not guaranteed activation. `true` was already the implicit policy default; making it explicit is not evidence of improved recall.
- [ChatGPT Skills](https://learn.chatgpt.com/docs/skills-and-plugins) and [ChatGPT tools and environments](https://learn.chatgpt.com/docs/use-chatgpt): account, surface and workspace controls matter independently of the Skill.
- [Claude Code Skills](https://code.claude.com/docs/en/skills) and [Claude custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): installation and matching guidance were inspected. The core description is kept under the help article's 200-character guidance; this is not proof of upload acceptance or compatibility certification.
- [DeepSeek with Codex](https://api-docs.deepseek.com/quick_start/agent_integrations/codex/): inspected the official integration page as documentation, without configuring providers or calling a model.
- [Agent Skills specification](https://agentskills.io/specification): the shared package convention does not make every host's fields or behavior identical.

No host installation, implicit/explicit activation, model behavior or project runtime was exercised in this review. The repository permits only static review. Source checks and packaging cannot establish trigger precision/recall, productivity gains, model compliance or cross-platform compatibility. Official documentation is the basis for intended use; actual account access and success remain unverified.

# Platform Compatibility

ThinkAlong uses the open Agent Skills convention, with a portable-instructions fallback. Shared instructions do not make every AI product support native Skill discovery or provide identical tools.

| Platform / host | Suggested use | Limitation |
| --- | --- | --- |
| Codex | Install the skill folder under `~/.agents/skills/think-along/` or project `.agents/skills/think-along/`; invoke with `$think-along`. | Host tools and permissions remain authoritative. |
| Claude Code | Install under `~/.claude/skills/think-along/` or project `.claude/skills/think-along/`. | Follow the current Claude Code skill-loading behavior. |
| Claude web | Upload the ZIP when custom Skills are available. | Availability and execution settings can vary. |
| ChatGPT web | Upload via the Skills UI if enabled for the account/workspace. | Availability depends on plan, workspace policy, and rollout. |
| DeepSeek through a compatible host | Use the host's supported Skill directory and model configuration. | The host controls file access, tools, and skill loading. |
| Plain chat UI without native Skills | Copy `adapters/portable-instructions.md` into custom instructions or a conversation. | This does not provide tools, memory, file access, or automatic activation. |

## Official references

- [Agent Skills specification](https://agentskills.io/specification)
- [Codex Skills](https://developers.openai.com/codex/skills)
- [ChatGPT Skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Claude custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [DeepSeek + Codex](https://api-docs.deepseek.com/quick_start/agent_integrations/codex/)
- [DeepSeek Deep Code](https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode/)

Folder installations must include the repository root `LICENSE` inside the installed `think-along/` folder; the generated ZIP includes it already. Keep the ZIP's single `think-along/` root and relative references intact. Inspect existing installation directories before upgrading to preserve local changes.

No platform installation or activation was exercised in this iteration. Current policy is static review only. Official documentation links describe intended installation, not evidence that it succeeded on a particular account or host. A future tested-platform claim requires separate authorization and actual installation/activation evidence.

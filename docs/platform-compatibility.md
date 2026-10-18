# Platform Compatibility

ThinkAlong uses the open Agent Skills file convention. A shared instruction file does not make every AI product support native Skill discovery or provide identical tools.

| Platform / host | Suggested use | Important limitation |
| --- | --- | --- |
| Codex | Install under `~/.agents/skills/think-along/` or project `.agents/skills/think-along/`; invoke with `$think-along`. | Host tools and permissions remain authoritative. |
| Claude Code | Install under `~/.claude/skills/think-along/` or project `.claude/skills/think-along/`. | Confirm current host behavior. |
| Claude web | Upload the ZIP when custom Skills are available for the account. | Availability and execution settings can vary. |
| ChatGPT web | Upload via the Skills UI if enabled for the account/workspace. | Availability depends on plan, workspace policy, and rollout. |
| DeepSeek via a compatible host | Use the host's supported Skill directory and model configuration. | The host determines file access, tools, and skill loading. |
| DeepSeek chat web or other plain chat UI | Copy `adapters/portable-instructions.md` into custom instructions or a conversation. | Manual instructions do not provide tools, memory, file access, or automatic activation. |

## Official references

- [Agent Skills specification](https://agentskills.io/specification)
- [Codex Skills](https://developers.openai.com/codex/skills)
- [ChatGPT Skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Claude custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [DeepSeek + Codex](https://api-docs.deepseek.com/quick_start/agent_integrations/codex/)
- [DeepSeek Deep Code](https://api-docs.deepseek.com/quick_start/agent_integrations/deepcode/)

Portability means reusable instructions, not identical platform features. Mark a platform as tested only after installing and exercising the Skill there.

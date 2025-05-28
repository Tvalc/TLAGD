# TLAGD+ API Sketch (Glitter Cloud Solutions)

TLAGD+ is a set of tools designed to prepare founders and teams to succeed in the new world of rapid, small-team product development. The API reflects all core and new capabilities described in the latest PRD.

## Core Endpoints

### `GET /personas`
- Returns a list of available product/dev personas (utility archetypes + legendary dev voices).

### `POST /critique`
- Input: `{ prompt: str, persona: str (optional) }`
- Output: `{ persona: str, feedback: str }`
- Description: Returns persona-driven feedback on a feature, system, or roadmap item.
- Token-gated: Unlock advanced personas/features based on user tier.

### `POST /backlog_analyze`
- Input: `{ backlog: [str], goals: str, tier: str (optional) }`
- Output: `{ prioritized: [str], rationale: str }`
- Description: Returns prioritized backlog with trade-off rationale (impact vs. dev lift), mapped to user-defined OKRs.

### `POST /mvp_simulate`
- Input: `{ gdd: str, deadline: str }`
- Output: `{ mvp_plan: str, experiment_suggestions: [str] }`
- Description: Suggests a lean MVP plan and what to test first, with explicit OKR mapping and rationale.

### `POST /founder_mode`
- Input: `{ deck: str, tokenomics: str, goals: str }`
- Output: `{ rewritten_pitch: str, viral_hook: str }`
- Description: Rewrites pitch decks/whitepapers in a game design-centric style, referencing business goals and OKRs.

### `POST /join_meeting`
- Input: `{ meeting_context: str, agenda: [str], okrs: [str] }`
- Output: `{ joined: bool, agent_participation_id: str }`
- Description: TLAGD+ agent joins a meeting (live/async), tracks discussion topics, and monitors OKR alignment.

### `POST /okr_focus_prompt`
- Input: `{ meeting_id: str, current_topic: str, okrs: [str] }`
- Output: `{ prompt: str }`
- Description: Prompts team when discussion drifts from declared OKRs or when a new OKR is needed.

### `POST /meeting_summary`
- Input: `{ meeting_id: str }`
- Output: `{ summary: str, editorial: [ { agent: str, recommendation: str, rationale: str, okr_reference: str } ] }`
- Description: Generates a meeting summary and editorialized recommendations, referencing which Developer Agent made each recommendation and why, with OKR mapping.

## Integration Examples
- Discord bot: `/critique`, `/prioritize`, and `/meeting_summary` commands trigger API calls, post feedback or summaries in channel.
- Web app: Upload backlog, GDD, or deck and receive actionable plans, persona-driven critique, and meeting/cycle management outputs.
- Token-gating: Endpoints/enhancements unlock with staked tokens or user tier.

# TLAGD+ API Sketch

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
- Description: Returns prioritized backlog with trade-off rationale (impact vs. dev lift).

### `POST /mvp_simulate`
- Input: `{ gdd: str, deadline: str }`
- Output: `{ mvp_plan: str, experiment_suggestions: [str] }`
- Description: Suggests a lean MVP plan and what to test first.

### `POST /founder_mode`
- Input: `{ deck: str, tokenomics: str, goals: str }`
- Output: `{ rewritten_pitch: str, viral_hook: str }`
- Description: Rewrites pitch decks/whitepapers in a game design-centric style.

## Integration Examples
- Discord bot: `/critique` and `/prioritize` commands trigger API calls, post feedback in channel.
- Web app: Upload backlog, GDD, or deck and receive actionable plans and persona-driven critique.
- Token-gating: Endpoints/enhancements unlock with staked tokens or user tier.

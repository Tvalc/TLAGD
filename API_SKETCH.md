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

---

## New & Enterprise Endpoints

### `GET /analytics/okr_progress`
- Input: `{ team_id: str, period: str }`
- Output: `{ okr_stats: [ { okr: str, progress: float, at_risk: bool } ] }`
- Description: Returns OKR progress and highlights at-risk objectives for a team or org.

### `GET /audit_logs`
- Input: `{ user_id: str, range: str }`
- Output: `{ logs: [ { action: str, timestamp: str, agent: str } ] }`
- Description: Lists all major actions, agent interventions, and recommendations for compliance and review.

### `POST /integrations/notion`
- Input: `{ notion_token: str, artifact_id: str }`
- Output: `{ exported: bool, notion_url: str }`
- Description: Exports a TLAGD+ artifact to Notion workspace.

### `POST /integrations/jira`
- Input: `{ jira_token: str, okr_id: str, ticket_data: dict }`
- Output: `{ created: bool, jira_url: str }`
- Description: Creates or updates a Jira ticket from an OKR or agent recommendation.

### `POST /integrations/slack`
- Input: `{ slack_token: str, message: str, channel: str }`
- Output: `{ posted: bool }`
- Description: Posts agent-attributed meeting summaries or recommendations to a Slack channel.

### `POST /integrations/google`
- Input: `{ google_token: str, artifact_id: str, type: str }`
- Output: `{ exported: bool, google_url: str }`
- Description: Exports an artifact to Google Slides, Docs, or Sheets.

### `POST /classroom_mode`
- Input: `{ educator_id: str, class_roster: [str], project_ids: [str] }`
- Output: `{ session_id: str, feedback: [ { student: str, agent_feedback: str } ] }`
- Description: Launches a collaborative classroom critique session.

---

## Open API & Integration Guide
- All endpoints accept and return JSON.
- Auth via OAuth2 or token-based headers (per-user, per-team, or per-educator).
- Rate limiting: 1000 requests/day for Free, 10,000 for Pro/Team, unlimited for Enterprise/Education.
- Webhooks available for artifact export and meeting summary delivery.
- Sample integration guides for Notion, Jira, Slack, Google Workspace provided in `/docs/integrations/`.

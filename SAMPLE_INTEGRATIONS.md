# TLAGD+ Sample Integration Guides

---

## Notion Integration
**Exporting Artifacts to Notion**
1. Go to Integrations > Notion in the TLAGD+ dashboard.
2. Connect your Notion account (OAuth).
3. Select the artifact to export (MVP plan, meeting summary, etc.).
4. Click 'Export to Notion' — confirm destination workspace/page.
5. View your artifact in Notion with agent-attributed annotations.

---

## Jira Integration
**Creating/Updating Jira Tickets from OKRs**
1. Go to Integrations > Jira.
2. Authenticate with your Jira account.
3. Map TLAGD+ OKRs or agent recommendations to Jira tickets.
4. Click 'Create/Update Ticket' — link appears in Jira.
5. Track progress and agent feedback directly in Jira.

**Context & Rationale:**
Jira integration turns agent-driven prioritization and OKR mapping into live, actionable tickets. This bridges the gap between strategy and execution, reducing manual work and ensuring alignment.

**User Journey:**
- PM uploads backlog or receives agent critique in TLAGD+.
- Syncs prioritized tasks, with agent commentary, directly to Jira boards.
- Developers see rationale, OKR links, and agent recommendations alongside each ticket.

**Business Impact:**
- Reduces miscommunication and rework.
- Makes product strategy defensible and transparent for engineering and leadership.
- Differentiates TLAGD+ from generic AI tools by closing the loop from insight to action.

---

## Slack Integration
**Posting Agent Summaries to Slack**
1. Go to Integrations > Slack.
2. Connect your Slack workspace.
3. Choose the channel for posting meeting summaries or recommendations.
4. Enable auto-post or send manually after each meeting.
5. Agent-attributed outputs appear in Slack with actionable next steps.

**Context & Rationale:**
Slack integration keeps teams in sync by delivering agent-attributed summaries, action items, and risk alerts where conversations happen.

**User Journey:**
- After a meeting or critique, TLAGD+ posts a summary and next steps to a chosen Slack channel.
- Team members can ask follow-up questions or trigger new agent sessions directly from Slack.

**Business Impact:**
- Increases visibility and accountability.
- Drives viral adoption as teams invite more collaborators.
- Supports premium tiers with advanced notification and workflow features.

---

## Google Workspace Integration
**Exporting Artifacts to Slides, Docs, or Sheets**
1. Go to Integrations > Google Workspace.
2. Authenticate with your Google account.
3. Select export type (Slides, Docs, Sheets) and artifact.
4. Click 'Export' — link appears in your Google Drive.
5. Share or present directly from Google Workspace.

**Context & Rationale:**
Google Workspace integration enables flexible export to Docs, Sheets, and Drive, supporting reporting, analytics, and collaboration.

**User Journey:**
- User exports meeting notes, analytics, or artifacts to Google Drive for sharing or compliance.
- Data can be imported into Sheets for custom analysis or shared with external stakeholders.

**Business Impact:**
- Reduces friction for Google-centric organizations.
- Enables compliance exports and audit trails for enterprise customers.
- Supports upsell to Team/Enterprise tiers with advanced analytics and export controls.

---

## Webhooks & API Automation
- Set up webhooks for artifact export, meeting summary delivery, or agent alerts.
- Use API tokens for automated workflows (see API_SKETCH.md for endpoint details).
- Example: Auto-export meeting summaries to Notion and Slack after each meeting.

---

*For more integration help, see the KNOWLEDGE_BASE.md or join our Discord community.*

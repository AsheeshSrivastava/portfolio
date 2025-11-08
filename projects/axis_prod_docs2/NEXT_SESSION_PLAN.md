# AXIS AI — Next Session Plan (Production Sprint 1)

## P1 — LangGraph Backbone
Nodes: Parse → CanonicalRetrieve → CoverageCheck → (WebPath?) → Synthesize → VerifyGrounding → FormatPSW → Gates → Return.
New endpoint: `/v1/chat` (keep /ask and /answer for debug).

## P2 — Conversation History
Sliding window per session id (bounded).

## P3 — Observability
LangSmith tracing; telemetry fields above.

## P4 — Canonical Ingestion
CLI or `/admin/canon/upsert` to validate schema, embed/chunk, upsert Canonical, invalidate WEI.

## P5 — WEI (Shared TTL Cache)
Allow-listed web snippets with `fetched_at` / `expires_at` / `license` / `checksum`.

## P6 — Eval Gate
25-case dataset; pre-merge gate: overall ≥85, groundedness ≥80%.

### Prep
- Branch `feature/axis-prod`
- 3–5 CanonicalContent samples
- Confirm allowlist
- OpenAI key ready (`/config`)

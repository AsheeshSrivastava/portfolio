# CanonicalContent — QC Output & Submission (v1.0)

**Output:** produce JSON files following `contracts/canonical_content.schema.json`.
Place files in `canonical/`, named `<content_id>@<version>.json`.

**Checks before PR**
- Rubric ≥85/100
- Gates pass: coverage ≥0.65, citation_density ≥1.0, exec_ok, scope_ok
- Citations include allow-listed, licensed sources (with anchors when possible)
- Index meta set: embedding_version, chunk_strategy_version, content_checksum (sha256 of body_markdown)

**PR**
- Title: `feat(canonical): add <content_id>@<version>`
- Body: short summary, license note, rubric overall, gates details.

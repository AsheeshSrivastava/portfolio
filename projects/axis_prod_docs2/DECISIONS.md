# AXIS AI — Production Decisions (v1.0)

## Roles & Boundaries
- Research Portal (later) creates; **Quality Checker (QC)** validates.
- QC outputs **CanonicalContent v1.0**; **Canonizer** (single writer) embeds/upserts Canonical; **AXIS** is read-only.

## Retrieval (Tiered)
1) Canonical → CoverageCheck
2) If low coverage → **WEI** (shared TTL web cache)
3) If still low → **Allow-listed Web** with corroboration ≥2
4) Fallback always generates **manual Evidence Pack** (for QC)

## Gates & Telemetry
- Gates now: `coverage ≥ 0.65`, `citation_density ≥ 1.0` (add `exec_ok`, `scope_ok` next).
- Telemetry: `model, latency_ms, coverage_score, citation_density, retrieval_source, fallback_trigger`.
- Label responses: `retrieval_source: canonical|wei|web|mixed`.

## Allowlist & Licensing
- Allowlist: docs.python.org, peps.python.org, numpy.org, pandas.pydata.org, matplotlib.org, seaborn.pydata.org, scikit-learn.org, DOI/journals.
- Store `license` on each citation; reject incompatible licenses from Canonical.

## Versioning & Indexing
- `index_meta`: `embedding_version`, `chunk_strategy_version`, `content_checksum (sha256(body_markdown))`.
- Any content change → bump SemVer, recompute checksum; re-embed when versions change.

## Modes & PSW
- Answers are **PSW JSON** and **mode-aware** (Coach/Hybrid/Socratic). Verify grounding after style.

## Scope
- Python core + {NumPy, pandas, Matplotlib, seaborn, scikit-learn}. Out-of-scope → helpful redirect.

# ClashRoyaleBuildABot — Agent Instructions

This is the canonical repository-level contract for work in `quantdale/ClashRoyaleBuildABot`. Harness-specific goal adapters are subordinate to this file.

## Repository and provenance boundary

This repository contains the Clash Royale Build-A-Bot codebase with local `quantdale` configuration/automation history. The README intentionally retains upstream-oriented attribution and links to `Pbatch/ClashRoyaleBuildABot` resources. Treat those external wiki/issues/Discord references as upstream/community context, not as authoritative local roadmap or local validation state. Read `LOCAL_REPOSITORY.md` for this distinction before using README roadmap/support links as planning inputs.

The repository's own legal disclaimer limits the software to educational/research purposes and states that use with the live Clash Royale game is prohibited. Agents must preserve that boundary: do not perform live-game automation, account interaction, anti-cheat bypass, or other activity that contradicts the repository's stated usage policy.

## Required reading

1. `LOCAL_REPOSITORY.md` and `README.md`, including the legal disclaimer.
2. `.agent/STATE.md` and `.agent/PLANNER_HANDOFF.md`.
3. `.agent/EXECUTION_PROMPT.md` if one exists; reconcile it with current `main` before resuming.
4. `pyproject.toml`, relevant workflows, tests, and source for any setup/compatibility claim.
5. `CONTRIBUTING.md` when contribution conventions are relevant.

## Current toolchain and validation

`pyproject.toml` currently requires Python `3.12.*` and defines the dependency groups. The lint workflow installs with `uv` and runs:

```bash
uv sync --extra cpu --extra dev
uv run ruff check .
uv run ruff format . --check
```

Use repository-defined workflows/configuration to discover additional build/test requirements rather than inventing commands. Never report a validation result that was not executed at the current checkout.

## Engineering and documentation discipline

- Preserve contributor attribution and upstream references unless a deliberate provenance cleanup is requested.
- Keep local-vs-upstream status explicit when editing roadmap, support, setup, or issue references.
- Do not silently upgrade pinned dependencies or Python constraints as part of unrelated work.
- Update living docs when setup, dependencies, workflows, GUI behavior, supported environments, or legal/product boundaries change.
- Historical commit messages and upstream issue links are historical/contextual evidence, not current local acceptance gates.

Evidence precedence:

`current executable validation` > `current local implementation/configuration` > `active local state/prompt` > `local living docs` > `upstream/historical context` > `assumptions`.

## Git safety

Inspect repository status and the final diff. Do not discard unrelated work, rewrite history, force-push, or use destructive cleanup. Keep local maintenance commits narrowly scoped and explicitly distinguish local changes from upstream-derived content.

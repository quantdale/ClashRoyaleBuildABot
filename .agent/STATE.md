# Current State

**Repository:** `quantdale/ClashRoyaleBuildABot`  
**State:** LOCAL_COPY_WITH_UPSTREAM_ORIENTED_DOCUMENTATION

## Durable truth

The repository contains a Python 3.12 Clash Royale Build-A-Bot codebase plus local configuration and cross-harness planner/executor adapters. The README retains upstream/community wiki, issue, Discord, contributor, and roadmap references; those links do not by themselves describe the current `quantdale` repository's roadmap or validation state. `LOCAL_REPOSITORY.md` records that provenance boundary.

Current `pyproject.toml` requires Python `3.12.*`. The committed lint workflow uses `uv`, installs CPU + dev extras, and runs Ruff check plus Ruff format check.

The repository's own legal disclaimer states educational/research-only intent and prohibits use with the live Clash Royale game. Preserve that boundary in future work.

## Validation status

This documentation sweep did not execute Python installation, lint, build, tests, emulator setup, or GUI/runtime validation. No fresh PASS is claimed.

## Continuation

Read `AGENTS.md`, then reconcile any future active execution prompt with current local `main`. Distinguish local requirements from upstream issue/wiki status, validate with repository-owned commands/workflows, and update this state when local product scope, toolchain, validation, or provenance changes.

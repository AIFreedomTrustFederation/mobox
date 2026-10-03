# AGENTS.md — AIFT MoBox Compatibility Runtime

## Scope

This repository is an upstream-derived fork of `olegos2/mobox`. It provides the Android/Termux Windows compatibility runtime used by the AIFT federation. Preserve upstream attribution and keep federation-specific integration isolated in `aift.repo.json`, `.aift/`, and `federation/` unless a runtime change genuinely requires touching upstream-derived files.

## Safety Boundaries

- Keep execution local-first, inspectable, and human initiated.
- Never add credentials, tokens, private endpoints, or user data to the repository.
- Do not silently download or execute new remote code during validation.
- Do not claim that a runtime, service, or federation adapter is healthy without executable evidence.
- Do not perform destructive Git operations, publish releases, or change upstream synchronization without human approval.
- Do not change licensing or remove upstream notices and attribution.

## Validation

Run the dependency-free source gate used by CI:

```sh
bash -n install
sh -n .aift/commands/status.sh
python3 federation/scripts/validate-index.py
git diff --check
test -z "$(git status --porcelain)"
```

Run additional targeted checks when changing installer behavior, runtime components, or Termux integration. Validation must not modify tracked files or leave generated artifacts behind.

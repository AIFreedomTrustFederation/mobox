# Federation Role: mobox

## Layer

`federated`

## Role

federated repository participating in the AIFT operating system

## Operating Principle

This repository is part of the AI Freedom Trust Federation operating system. It remains sovereign in its own repo while participating in the shared federation control plane.

## Control Plane

Top-level workspace:

```bash
/data/data/com.termux/files/home/AIFT
```

Primary command:

```bash
/data/data/com.termux/files/home/AIFT/aift-os.sh
```

## Standard Commands

Status:

```bash
git status --short
```

Pull:

```bash
git pull --ff-only
```

Verify (run from the repository root; requires Bash, POSIX sh, and Python 3):

```bash
bash -n install && sh -n .aift/commands/status.sh && python3 -B federation/scripts/validate-index.py
```

This read-only check validates shell syntax and local federation JSON registry references. It mirrors the source checks in `.github/workflows/verify.yml`. It does **not** install MoBox, exercise Wine/Box64 or Android hardware, verify external downloads, or prove runtime compatibility. `git status --short` is only a working-tree status command, not a verification test.

## Federation Metadata

This repo declares its federation role in:

```bash
aift.repo.json
```

The workspace-level federation manifest is generated at:

```bash
/data/data/com.termux/files/home/AIFT/manifests/workspace.json
```

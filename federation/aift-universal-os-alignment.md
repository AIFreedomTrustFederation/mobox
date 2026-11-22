# mobox — AIFT Universal OS Alignment

> **Planning document only.** The proposed AIFT OS is not proven installed, bootable on an arbitrary device or operating as an authenticated hosted desktop. This fork/project retains its own authority, instructions and upstream credits. See [central architecture and infographics in AIFT-OS PR #92](https://github.com/AIFreedomTrustFederation/AIFT-OS/pull/92).

## Existing scope

Upstream-derived Android/Termux Wine/Box64 application compatibility runtime, not a Windows bootloader, BIOS, native macOS layer or general phone OS.

## Proposed opt-in application contract

An explicitly optional application compatibility adapter for supported AIFT desktop/hosted contexts, with truthful local hardware and upstream capability reporting. Preserve olegos2/mobox attribution, installer and license notices.

~~~mermaid
flowchart LR
  SOURCE["mobox: current project authority"] --> ADAPTER["Optional versioned app / capability adapter"]
  ADAPTER -. "only if tested" .-> OS["AIFT native / hosted desktop"]
  USER["Explicit owner grants"] --> ADAPTER
  TEST["Device-specific tests and rollback"] --> ADAPTER
~~~

## Measurable milestones

1. Verify source license/ownership, README and AGENTS constraints before any implementation.
2. Specify app entrypoint, supported host/device targets, local data boundaries, required permissions and unavailable state.
3. Add independent regression tests proving authorization, opt-out and actual operation; reject a visual mock as deployment evidence.
4. Document Bash installer syntax, federation index validator, source QA, supported Android/Termux execution acceptance and honest unavailable state.
5. Publish an exact-head artifact/log and downstream consumer test before claiming integration.

## Explicit safety and non-goals

No new remote code downloads during verification, credential propagation, actual device flashing, automatic install or claims of native Windows boot support. Device firmware, Apple boot policy, Windows boot entries, robot actuation and production release remain out of scope for this docs proposal.

[Central OS platform proposal](https://github.com/AIFreedomTrustFederation/AIFT-OS/pull/92).

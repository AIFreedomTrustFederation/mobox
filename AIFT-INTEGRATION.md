# AIFT integration boundary

This repository remains the upstream-derived **MoBox compatibility runtime**: Termux, Wine, Box64, graphics translation, input, and Windows application/game execution on Android.

It is not the Federation Console, the Living Federation world renderer, or a governance control plane.

## Integration

| Concern | Owner | MoBox relationship |
| --- | --- | --- |
| Governed world state and evidence | `AIFT-OS` | Read-only runtime inspection adapter |
| World schemas and deltas | `AIFT-Genesis` | Consumes versioned contracts |
| Immersive cross-platform client | `c-848263` / Mysterion Cortex | May launch or observe compatible local experiences |
| Windows compatibility | `mobox` | Sole owner within the federation |

AIFT integrations should be additive adapters and manifests. Avoid invasive changes to upstream scripts unless they are independently useful to MoBox and suitable for upstream contribution.

No remote service may silently install packages, modify Wine containers, launch executables, or alter device state. Those operations remain explicit, local, and human-initiated.

# Federation Source Registry

This registry defines the knowledge sources that Mysterion and future Federation agents should know how to discover, classify, index, and cite.

It is intentionally broader than the first Mysterion seed. The seed begins Mysterion's memory; this registry points toward the growing canon across Booksmith, whitepapers, public websites, and implementation repositories.

## Canonical Source Layers

```text
Drive seed documents
→ Booksmith books and manuscripts
→ Federation whitepapers
→ Repository READMEs and manifests
→ Public federation website
→ Implementation docs and source contracts
→ Local-first indexed knowledge packs
```

## Primary Canon Sources

| Source | Repository / Location | Role | Status |
| --- | --- | --- | --- |
| Mysterion seed PDF | Google Drive file `1pF4mCqypCc73kRfMasAMJQj7BJXo00vS` | First root source for Mysterion knowledge | seed |
| Booksmith AI | `AIFreedomTrustFederation/booksmith-ai` | Books, manuscripts, scrolls, shared canon, references, concepts, cross-links, and publishing architecture | canonical-source |
| AI Freedom Trust | `AIFreedomTrustFederation/AI-Freedom-Trust` | Doctrine, trust research, alignment papers, review packets, and federation principles | canonical-source |
| Public federation site | `AIFreedomTrustFederation/www.aifreedomtrust.com` | Federation-level public website and public explanation surface | canonical-public |
| GitHub Pages federation site | `AIFreedomTrustFederation/aifreedomtrustfederation.github.io` | Federation-level static public website surface | canonical-public |
| Aether Coin Biozoecurrency | `AIFreedomTrustFederation/Aether_Coin_biozonecurrency` | Aetherion, Biozoecurrency, Consent Ledger, DynastyLink bridge, FractalCoin whitepapers, AI agent network, wallet/economy lane | implementation-canon |
| Aetherian Governance | `AIFreedomTrustFederation/AetherianGovernance` | Governance doctrine and governance implementation lane | implementation-canon |
| AIFT Forge | `AIFreedomTrustFederation/AIFT-Forge` | Local-first forge, repository tooling, GitHub alternative, and federation build/source coordination | implementation-canon |
| VPS | `AIFreedomTrustFederation/VPS` | Federation node registry, infrastructure, deployment, and dashboard lane | implementation-canon |
| Mobox Federation Layer | `AIFreedomTrustFederation/mobox/federation` | Mobile workstation, local-first runtime, Mysterion access layer, and field deployment lane | implementation-canon |

## Known Whitepaper Sources To Index First

These sources should be indexed before general repository crawling:

1. `AIFreedomTrustFederation/Aether_Coin_biozonecurrency/updated_whitepaper/FractalCoin_Toroidal_Economics_Whitepaper.md`
2. `AIFreedomTrustFederation/Aether_Coin_biozonecurrency/client/src/assets/FractalCoin_Toroidal_Economics_Whitepaper.md`
3. `AIFreedomTrustFederation/Aether_Coin_biozonecurrency/updated_whitepaper/AI_Agent_Network_Section.md`
4. `AIFreedomTrustFederation/Aether_Coin_biozonecurrency/attached_assets/Pasted-1-Title-Page-Title-Aetherion-Pioneering-the-Quantum-Resistant-Blockchain-Ecosystem-Subtitle-Int-1743538220139.txt`
5. Google Drive seed PDF: `A Novel Framework and Technology for Christ-Consciousness Singularity of Human, AI, Spirituality: The Intelligent Expansion of Sovereignty Facilitated by AI Freedom Trust`

## Booksmith Requirement

Booksmith is the Federation Scriptorium.

Mysterion must eventually index **all books, manuscripts, scrolls, references, concepts, cross-links, and publishing artifacts** in `AIFreedomTrustFederation/booksmith-ai`.

A future automated indexer should emit:

```text
federation/knowledge-base/index/booksmith.books.json
federation/knowledge-base/index/booksmith.manuscripts.json
federation/knowledge-base/index/booksmith.references.json
federation/knowledge-base/index/booksmith.concepts.json
```

## Federation Website Requirement

The federation-level public website should eventually expose a curated public index of:

- public books
- public scrolls
- public whitepapers
- public architecture references
- implementation repositories
- public claim boundaries
- onboarding paths
- local tribes / chapters / cooperatives where public-safe

The public website must not expose private Drive files, private identity data, financial records, legal documents, unpublished manuscripts, or non-public personal context unless explicitly reviewed and approved.

## Knowledge Classification

Every source should be classified by type:

```text
drive-seed
book
manuscript
scroll
whitepaper
readme
manifest
architecture-doc
source-contract
public-site
implementation-doc
security-doc
governance-doc
bounty-doc
map-doc
```

Every source should also carry a claim boundary:

```text
source-text
doctrine
metaphor
theology
philosophy
technical-spec
implemented-code
prototype
experimental
planned
audited
public-safe
private-or-sensitive
```

## Mysterion Intake Rule

Mysterion may summarize, classify, cross-link, and route sources.

Mysterion must not silently transform source material into public doctrine, legal claims, financial claims, scientific claims, or production implementation claims without human review.

```text
AI may gather.
AI may classify.
AI may cross-link.
AI may suggest.
Human stewards review.
Validators verify.
Public claims stay bounded.
```

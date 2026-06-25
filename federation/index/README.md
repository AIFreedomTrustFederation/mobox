# Federation Root Index

The Federation Root Index is the trunk-level table of contents for Mysterion, human contributors, local AI gardeners, Scroll Keepers, validator nodes, and public-safe website publishing.

This directory does not duplicate the full Federation. It points to canonical sources and defines the minimum index structure needed to discover, classify, cross-link, and validate the Federation as it grows.

## Purpose

The Federation needs more than scattered repository search. It needs a structured, living index that can answer:

- What repositories exist?
- What does each repository implement?
- What books, Scrolls, and whitepapers exist?
- Which concepts are canonical?
- Which ideas are implemented in code?
- Which AI agents may access which knowledge scopes?
- Which sources are public-safe?
- Which sources require human review before publication?

## Index Layers

```text
Federation Root Index
├── Repository Registry
├── Knowledge Registry
├── Concept Registry
├── Implementation Registry
├── Agent Registry
├── Community Registry
├── Bounty Registry
└── Public Website Registry
```

## First Files

```text
federation/index/repositories.json
federation/index/concepts.json
federation/index/implementations.json
federation/index/agents.json
federation/index/public-website.json
```

## Operating Principle

Mysterion should not guess where doctrine, code, books, or whitepapers live.

Mysterion should read the index, follow the manifest trail, classify sources, and preserve claim boundaries.

```text
Index first.
Crawl second.
Summarize third.
Implement fourth.
Publish only after review.
```

## Main Repo Rule

This index is being built directly in the main `AIFreedomTrustFederation/mobox` repository to avoid clone drift, rebase overhead, and disconnected knowledge branches.

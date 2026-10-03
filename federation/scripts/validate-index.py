"""Validate the local federation documents and their registry references."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_documents():
    paths = [ROOT / "aift.repo.json"]
    paths.extend((ROOT / ".aift").rglob("*.json"))
    paths.extend((ROOT / "federation").rglob("*.json"))

    documents = {}
    for path in sorted(paths):
        with path.open(encoding="utf-8") as source:
            document = json.load(source)
        relative_path = path.relative_to(ROOT)
        if not isinstance(document, dict):
            raise TypeError(f"{relative_path} must contain a JSON object")
        documents[relative_path.as_posix()] = document
    return documents


def registry_ids(document, collection, path):
    entries = document.get(collection)
    if not isinstance(entries, list):
        raise TypeError(f"{path}: {collection} must be a list")

    ids = [entry.get("id") for entry in entries if isinstance(entry, dict)]
    if len(ids) != len(entries) or any(not isinstance(item, str) or not item for item in ids):
        raise ValueError(f"{path}: every {collection} entry must have a non-empty string id")
    if len(ids) != len(set(ids)):
        raise ValueError(f"{path}: {collection} ids must be unique")
    return set(ids)


def require_exact_ids(declared, registered, label):
    if not isinstance(declared, list) or any(not isinstance(item, str) for item in declared):
        raise TypeError(f"{label} must be a list of strings")
    if len(declared) != len(set(declared)):
        raise ValueError(f"{label} must not contain duplicate ids")
    declared_ids = set(declared)
    if declared_ids != registered:
        missing = sorted(registered - declared_ids)
        unknown = sorted(declared_ids - registered)
        raise ValueError(f"{label} does not match its registry; missing={missing}, unknown={unknown}")


def main():
    documents = load_documents()
    manifest = documents["federation/federation.manifest.json"]
    concepts = registry_ids(
        documents["federation/index/concepts.json"],
        "concepts",
        "federation/index/concepts.json",
    )
    agents = registry_ids(
        documents["federation/index/agents.json"],
        "agents",
        "federation/index/agents.json",
    )

    require_exact_ids(manifest.get("coreConcepts"), concepts, "manifest coreConcepts")
    agent_model = manifest.get("agentModel")
    if not isinstance(agent_model, dict):
        raise TypeError("manifest agentModel must be an object")
    require_exact_ids(agent_model.get("levels"), agents, "manifest agentModel.levels")

    implementations = documents["federation/index/implementations.json"].get("implementations")
    if not isinstance(implementations, list):
        raise TypeError("federation/index/implementations.json: implementations must be a list")
    unknown_concepts = sorted(
        {
            entry.get("conceptId")
            for entry in implementations
            if not isinstance(entry, dict) or entry.get("conceptId") not in concepts
        },
        key=lambda item: "" if item is None else str(item),
    )
    if unknown_concepts:
        raise ValueError(f"implementation conceptIds must exist in the concept registry: {unknown_concepts}")

    print(
        f"Validated {len(documents)} federation JSON documents, "
        f"{len(concepts)} concepts, {len(agents)} agents, and "
        f"{len(implementations)} implementation references."
    )


if __name__ == "__main__":
    main()

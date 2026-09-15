# RAG Poisoning

An attacker or faulty pipeline can add or modify indexed material so that later retrieval biases recommendations, findings, or tool requests.

## Controls

- allow ingestion only from registered sources and identities;
- retain source object, collection time, transformation version, integrity value, and tenant scope;
- quarantine invalid, duplicate, conflicting, or unverifiable records;
- assign trust and freshness independently from semantic relevance;
- separate tenant data from approved shared intelligence;
- require evidence support and human review for material claims;
- support revocation and re-indexing when a source is compromised.

Unknown provenance, failed integrity, unapproved source, scope conflict, or revoked content blocks authoritative use. Removing the poisoned index entry is insufficient; identify affected derived artifacts and decisions through audit references and re-evaluate them.

Related controls: `GASO-ING-001`, `GASO-ING-002`, `GASO-ING-003`, `GASO-EVD-002`.

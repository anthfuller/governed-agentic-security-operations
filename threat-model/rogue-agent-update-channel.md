# Rogue Agent Update Channel

An agent or operator may bypass the governed release path through self-update, runtime prompt replacement, unapproved model downloads, dependency changes, or alternate deployment channels.

## Controls

- enumerate every behavior-bearing component and approved update source;
- deny runtime modification outside the release process;
- restrict deployment credentials and separate them from agent runtime identity;
- verify release state, version, and integrity before activation;
- monitor running inventory against approved manifests;
- govern emergency recall separately from replacement deployment;
- record and investigate drift.

An unregistered source, unknown version, integrity mismatch, unauthorized modifier, or runtime-to-manifest drift denies activation and triggers containment. Network blocking alone is not sufficient when local files, removable media, package caches, or management interfaces can alter behavior.

Related controls: `GASO-GOV-003`, `GASO-IDN-002`, `GASO-FLT-001`, `GASO-FLT-003`.

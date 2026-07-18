# Repository 1 Revision Report - July 18, 2026

This report records the publication-preparation changes made to the uploaded local snapshot of `constructible-cubic-trisection`.

## Manuscript changes

No theorem statement, displayed coefficient, numerical table value, or principal mathematical claim was altered.

The following scholarly and publication edits were made:

- added PDF title, author, subject, and keyword metadata;
- added the canonical repository URL and version number to the title page;
- added explicit citations to Wantzel and Dudley for the classical impossibility context;
- added an explicit acknowledgement of Rostamian's analysis of Baker's seed construction and first iterative improvement;
- corrected and expanded the Rostamian bibliography entry;
- reordered the bibliography to match first citation order;
- noted the standalone verification scripts in the reproducibility appendices;
- recompiled and visually checked the 11-page PDF.

## Repository changes

- replaced the starter README with a publication-oriented README;
- embedded the finalized Repo 1 infographic;
- rewrote `CITATION.cff` using a schema-valid top-level software/source-archive record and an unpublished-paper `preferred-citation`;
- expanded the changelog and reproducibility record;
- added pinned Python dependencies;
- added exact symbolic and 100-decimal-digit numerical verification scripts;
- generated committed text and CSV outputs;
- replaced the first-upload checklist with a release checklist;
- added GitHub release notes for `v1.0.0`;
- updated repository and paper-folder descriptions.

## Items intentionally deferred

- **DOI:** add after the tagged GitHub release is archived.
- **Cross-repository links:** activate after the companion repositories have stable public URLs.
- **License:** the newer GitHub repository already uses CC BY 4.0 for research materials and MIT for source code. The publication package now preserves that dual-license structure.

## GitHub synchronization caution

The GitHub repository may contain edits that are newer than the uploaded ZIP. Before replacing a file on GitHub, compare the current GitHub version against this package, especially:

```text
README.md
CITATION.cff
LICENSE, LICENSE-PAPER.md, or LICENSE_NOTICE.MD
paper/constructible_cubic_trisection.tex
```

The files in this package are internally synchronized and validated as a set.

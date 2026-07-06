# GitHub Upload Checklist

Use this checklist for the first public upload.

## 1. Create the repository

Suggested repository name:

```text
constructible-cubic-trisection
```

Suggested short description:

```text
A straightedge-and-compass constructible cubic error cascade for approximate angle trisection.
```

Suggested visibility for first setup:

```text
Private first, then public after final review.
```

## 2. Add files

Upload these first:

```text
README.md
CITATION.cff
REPRODUCIBILITY.md
LICENSE_NOTICE.md
CHANGELOG.md
.gitignore
paper/constructible_cubic_trisection.tex
paper/README.md
docs/abstract.md
docs/github_upload_checklist.md
docs/repository_description.md
```

Optional but recommended before public release:

```text
paper/constructible_cubic_trisection.pdf
LICENSE
```

## 3. GitHub About section

Use the description from `docs/repository_description.md`.

Suggested topics:

```text
geometry
angle-trisection
straightedge-and-compass
constructible-geometry
asymptotic-analysis
error-cascade
latex
mathematics
```

## 4. First commit message

Suggested commit message:

```text
Initial preprint archive for constructible cubic trisection cascade
```

## 5. Public-release check

Before switching the repository to public, confirm:

- The PDF compiles from the uploaded source.
- The title, author, and date are correct.
- The README clearly says this is approximate trisection, not exact trisection.
- A final license has been selected.
- Citation metadata is present in `CITATION.cff`.
- Any code/output files are either included or clearly marked as future additions.

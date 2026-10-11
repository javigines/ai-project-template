#!/usr/bin/env python3
"""Basic, dependency-free checks for the generic AI project scaffold.

This is NOT secret scanning, YAML schema validation or application test coverage.
"""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs/PROJECT_CHARTER.md",
    "docs/ARCHITECTURE.md",
    "docs/GOVERNANCE.md",
    "docs/WORKFLOW.md",
    "docs/QUALITY_GATES.md",
    "docs/ROADMAP.md",
    "docs/SECURITY.md",
    "docs/RUNBOOK.md",
    "docs/decisions/README.md",
    "docs/decisions/ADR-0000-template.md",
    "docs/templates/ITERATION_MANDATE.md",
    "docs/templates/HANDOFF.md",
    "docs/templates/RESEARCH_REPORT.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/task.yml",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/research.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
]

errors = []
for name in REQUIRED:
    path = ROOT / name
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"Required nonempty file missing: {name}")

for document in list(ROOT.rglob("*.md")):
    if ".git" in document.relative_to(ROOT).parts:
        continue
    body = document.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        target = target.strip().strip("<>").split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "/", "#")):
            continue
        location = (document.parent / unquote(target)).resolve()
        if location != ROOT and ROOT not in location.parents:
            errors.append(f"Link escapes repository: {document.relative_to(ROOT)} -> {target}")
        elif not location.exists():
            errors.append(f"Broken relative link: {document.relative_to(ROOT)} -> {target}")

result = subprocess.run(
    ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=False
)
if result.returncode == 0:
    for name in result.stdout.splitlines():
        p = Path(name)
        if (
            any(segment in {"secrets", "private", "exports", "backups"} for segment in p.parts)
            or p.name == ".env"
            or p.suffix.lower() in {".pem", ".p12", ".pfx"}
        ):
            errors.append(f"Suspicious tracked path: {name}")

if errors:
    for error in errors:
        print(f"FAIL: {error}", file=sys.stderr)
    sys.exit(1)
print(f"PASS: structure, links and tracked-path checks ({len(REQUIRED)} required files).")
print("NOTE: run language-specific tests, secret scanning and security gates separately.")

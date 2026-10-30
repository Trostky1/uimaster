#!/usr/bin/env python3
"""Structure checks for the merged uimaster plugin.

The S1 tests (UX Agent Skills) guard the audit components. These checks guard what the merge
added: names, counts, the 20 laws, link integrity, the safety defaults, and the rulings log.

Run: `python3 tests/test_uimaster.py` (exit 0 = pass, 1 = fail).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

SKILLS = {"uimaster", "ux-laws", "taste", "craft", "usability-audit", "ux-audit",
          "spec-cuj", "audit-cuj", "render-report"}
S1_SKILLS = {"usability-audit", "ux-audit", "spec-cuj", "audit-cuj", "render-report"}
S1_COMMANDS = {"cuj-audit", "usability-audit", "ux-audit", "ux-review", "ux-spec"}
S1_AGENTS = {"usability-auditor", "cuj-author", "cuj-auditor"}
COMMANDS = S1_COMMANDS | {
    "design", "critique", "shape", "polish", "distill", "bolder", "quieter", "harden", "onboard",
    "animate", "colorize", "typeset", "layout", "delight", "overdrive", "clarify", "adapt",
    "optimize", "design-init", "design-document", "design-extract", "design-hooks",
    "design-doctor"}
AGENTS = S1_AGENTS | {"design-critic", "impeccable-documenter", "impeccable-asset-producer",
                      "impeccable-finish-reviewer"}
TOPICS = ["modes", "type", "colour", "layout", "motion", "states-forms", "accessibility",
          "responsive", "copy", "flows", "operate", "bans-and-tells", "audit-checks"]
LAWS = ["Hick", "Fitts", "Jakob", "Proximity", "Miller", "Doherty", "Von Restorff", "Fitts",
        "Serial Position", "Peak-End", "Zeigarnik", "Prägnanz", "Hick", "Postel", "Postel",
        "Similarity", "Uniform Connectedness", "Parkinson", "Tesler", "Goal-Gradient"]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_RE = re.compile(r"`[^`]*`")


def _fm(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def _req(cond: bool, msg: str, errs: list[str]) -> None:
    if not cond:
        errs.append(msg)


def check_skills() -> list[str]:
    errs: list[str] = []
    found = {p.parent.name for p in ROOT.glob("skills/*/SKILL.md")}
    _req(found == SKILLS, f"skills: expected {sorted(SKILLS)}, found {sorted(found)}", errs)
    for name in sorted(found):
        path = ROOT / "skills" / name / "SKILL.md"
        fm = _fm(path)
        _req(fm.get("name") == name, f"skill {name}: frontmatter name must be {name!r}", errs)
        desc = str(fm.get("description", "")).strip()
        _req(len(desc) > 40 and desc != ">-", f"skill {name}: needs a real description", errs)
        _req(len(path.read_text(encoding="utf-8").splitlines()) <= 500,
             f"skill {name}: SKILL.md must stay under 500 lines", errs)
    return errs


def check_commands_agents() -> list[str]:
    errs: list[str] = []
    cmds = {p.stem for p in (ROOT / "commands").glob("*.md") if p.name != "README.md"}
    _req(cmds == COMMANDS, f"commands: missing {sorted(COMMANDS - cmds)}, "
                           f"extra {sorted(cmds - COMMANDS)}", errs)
    for name in sorted(cmds):
        fm = _fm(ROOT / "commands" / f"{name}.md")
        _req(fm.get("name") == name, f"command {name}: frontmatter name mismatch", errs)
        _req(bool(str(fm.get("description", "")).strip()), f"command {name}: no description", errs)
        _req("argument-hint" in fm, f"command {name}: needs argument-hint", errs)
    agents = {p.stem for p in (ROOT / "agents").glob("*.md") if p.name != "README.md"}
    _req(agents == AGENTS, f"agents: missing {sorted(AGENTS - agents)}, "
                           f"extra {sorted(agents - AGENTS)}", errs)
    for name in sorted(agents):
        fm = _fm(ROOT / "agents" / f"{name}.md")
        _req(fm.get("name") == name, f"agent {name}: frontmatter name mismatch", errs)
    critic = (ROOT / "agents" / "design-critic.md").read_text(encoding="utf-8")
    _req("tools: Read, Grep, Glob" in critic, "design-critic must be read-only", errs)
    _req(S1_SKILLS <= {p.parent.name for p in ROOT.glob("skills/*/SKILL.md")},
         "S1 skill names must not change", errs)
    return errs


def check_laws() -> list[str]:
    errs: list[str] = []
    text = (ROOT / "skills" / "ux-laws" / "SKILL.md").read_text(encoding="utf-8")
    heads = re.findall(r"^## (\d+)\. (.+)$", text, re.M)
    nums = [int(n) for n, _ in heads]
    _req(nums[:20] == list(range(1, 21)), f"ux-laws: items 1-20 must be present, got {nums}", errs)
    for (n, title), law in zip(heads[:20], LAWS):
        _req(law.lower() in title.lower(), f"ux-laws: item {n} must name {law!r}, got {title!r}", errs)
    _req("Implementation Requirements" in text, "ux-laws: Implementation Requirements missing", errs)
    _req("prioritize clarity, accessibility, user control, and successful task completion"
         in text, "ux-laws: conflict rule missing", errs)
    _req("Cross-references (repeated laws)" in text, "ux-laws: cross-reference table missing", errs)
    return errs


def check_master() -> list[str]:
    errs: list[str] = []
    skill = (ROOT / "skills" / "uimaster" / "SKILL.md").read_text(encoding="utf-8")
    for topic in TOPICS:
        p = ROOT / "skills" / "uimaster" / "references" / f"{topic}.md"
        _req(p.exists(), f"master: missing references/{topic}.md", errs)
        _req(f"references/{topic}.md" in skill, f"master SKILL.md must link {topic}.md", errs)
    for cmd in COMMANDS:
        if cmd in ("cuj-audit", "ux-spec", "design-hooks", "design-doctor", "design-init",
                   "design-document", "design-extract"):
            continue
        _req(f"`/{cmd}`" in skill or f"`/{cmd}` " in skill or f"/{cmd}`" in skill,
             f"master SKILL.md command table should mention /{cmd}", errs)
    for ref in ("ux-laws.md", "design-critique.md"):
        _req((ROOT / "skills" / "usability-audit" / "references" / ref).exists(),
             f"usability-audit: missing references/{ref}", errs)
    return errs


def check_links() -> list[str]:
    errs: list[str] = []
    files: list[Path] = []
    for pat in ("skills/uimaster/**/*.md", "skills/ux-laws/*.md", "skills/craft/**/*.md",
                "skills/taste/*.md", "skills/taste/references/*.md",
                "skills/usability-audit/references/ux-laws.md",
                "skills/usability-audit/references/design-critique.md",
                "commands/*.md", "agents/*.md", "README.md", "hooks/README.md"):
        files += sorted(ROOT.glob(pat))
    for path in files:
        text = INLINE_RE.sub("", FENCE_RE.sub("", path.read_text(encoding="utf-8")))
        for m in LINK_RE.finditer(text):
            href = m.group(1).split()[0]
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = href.split("#", 1)[0]
            if target and not (path.parent / target).resolve().exists():
                errs.append(f"{path.relative_to(ROOT)}: broken link -> {href}")
    return errs


def check_safety_and_scope() -> list[str]:
    errs: list[str] = []
    hooks = json.loads((ROOT / "hooks" / "hooks.json").read_text(encoding="utf-8"))
    _req(hooks.get("hooks") == {}, "hooks.json must ship no active hooks (CONFLICTS C16)", errs)
    craft = (ROOT / "skills" / "craft" / "SKILL.md").read_text(encoding="utf-8")
    _req("Engine gate" in craft, "craft: engine gate missing from Setup", errs)
    for gone in ("live.md", "live-setup.md", "generate.md", "craft.md"):
        _req(not (ROOT / "skills" / "craft" / "reference" / gone).exists(),
             f"craft: reference/{gone} must not ship (live mode deferred)", errs)
    for js in (ROOT / "skills" / "craft" / "scripts").glob("live-browser*.js"):
        errs.append(f"craft: live-mode script must not ship: {js.name}")
    for path in (ROOT / "skills" / "craft").rglob("*.md"):
        _req("/impeccable " not in path.read_text(encoding="utf-8"),
             f"{path.relative_to(ROOT)}: stale '/impeccable <command>' mention", errs)
    plug = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    mkt = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    _req(plug.get("name") == "uimaster", "plugin.json name must be uimaster", errs)
    _req(plug.get("dependencies") == mkt["plugins"][0].get("dependencies"),
         "marketplace.json must mirror plugin.json dependencies", errs)
    return errs


def check_docs_and_licenses() -> list[str]:
    errs: list[str] = []
    conflicts = (ROOT / "CONFLICTS.md").read_text(encoding="utf-8")
    for i in range(1, 19):
        _req(f"| C{i} |" in conflicts, f"CONFLICTS.md: ruling C{i} missing", errs)
    lic = (ROOT / "LICENSES.md").read_text(encoding="utf-8")
    for s in ("Carl Sziebert", "Leonxlnx", "Paul Bakaus", "ehmo", "ux-laws-design"):
        _req(s in lic, f"LICENSES.md must mention {s}", errs)
    attr = (ROOT / "ATTRIBUTION.md").read_text(encoding="utf-8")
    for s in ("UX Agent Skills", "taste-skill", "impeccable", "ux-laws-design"):
        _req(s in attr, f"ATTRIBUTION.md must mention {s}", errs)
    for f in ("LICENSE-ux-agent-skills-MIT", "LICENSE-taste-skill-MIT",
              "LICENSE-impeccable-Apache-2.0", "NOTICE-impeccable.md"):
        _req((ROOT / "licenses" / f).exists(), f"licenses/{f} missing", errs)
    return errs


CHECKS = (check_skills, check_commands_agents, check_laws, check_master, check_links,
          check_safety_and_scope, check_docs_and_licenses)


def main() -> int:
    failures = [e for c in CHECKS for e in c()]
    if failures:
        print("FAIL — uimaster:")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(f"PASS — uimaster ({len(CHECKS)} checks: skills, commands/agents, laws, "
          f"master, links, safety, docs/licenses)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

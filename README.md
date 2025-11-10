# **Archon Prime V3 - The Self-Correcting System**

This repository is the complete, self-contained operating system for a solo founder executing the "Concierge MVP" of the Archon project. It is built on the principles of **leverage, automation, and focus**.

This V3 version represents a major upgrade, refactoring the system's core data files to use robust YAML frontmatter. This enables a powerful and reliable automation layer, moving beyond manual checklists to true operational leverage.

---

## **Part 1: The Repository Structure (The Digital Workshop)**

*   `app/`: The **ENGINEER** Hat - The Concierge MVP itself.
*   `docs/`: The **STRATEGIST** Hat - The strategic canon and playbooks.
*   `experiments/`: The **SCIENTIST** Hat - The lab notebook, now with machine-readable YAML data.
*   `scripts/`: The **OPERATOR** Hat - The V2 automation layer.
*   `tests/`: The formal testing framework for the toolkit.
*   `.github/workflows/`: The CI pipeline that automatically runs `pytest`.

---

## **Part 2: The Workflow (The Operating Cadence)**

This is the repeatable weekly cadence using the **V2 Automation Layer**.

**Phase 1: Recruitment**
1.  **Prospecting**: Run `python scripts/prospector.py --keywords "B2B SaaS"` to generate a CSV of leads. The script will then guide you to interactively select and append the best leads to the `experiments/00_RECRUITMENT_PIPELINE.md` file.
2.  **Outreach**: Run `python scripts/messenger.py`. This powerful script automatically finds all prospects with the 'Identified' status and walks you through the "Forced Personalization" workflow for each one.
3.  **Onboarding**: Once a team commits, run `python scripts/onboarder.py`. This script is a fully automated tool that updates the recruitment pipeline, creates the new team entry in the experiment tracking file, and prepares you to send the welcome email.

**Phase 2: Experiment Execution**
1.  **Prep (1 min before each session)**: Run `python scripts/session_prep.py --team "Alpha"`. This script now automatically generates a full session briefing, pulling the latest data from the YAML frontmatter and the latest notes from the markdown content.
2.  **Execute Session (60 mins)**: Follow the checklist in `docs/03_FACILITATOR_PLAYBOOK.md`.
3.  **Post-Session Analysis (15 mins)**:
    *   Run `python scripts/analyze_compass.py --file /path/to/new.json`.
    *   Update the YAML and markdown notes in `experiments/01_EXPERIMENT_TRACKING.md`.

**Phase 3: System Improvement (Weekly)**
*   **Review and Reflect**: Read through all your notes in the experiment tracking file.
*   **Improve the System**: The system is designed for self-correction. If a script is clunky or a workflow has friction, dedicate a few hours to improving it. Add a new test, then refactor the code.

---

This system is the trusted foundation for the Archon project, enabling a single operator to perform at an elite level.

# **Archon Prime V2.0 - Execution Toolkit**

This repository is the complete, self-contained operating system for a solo founder executing the "Concierge MVP" of the Archon project. It is built on the principles of **leverage, automation, and focus**.

Its purpose is to externalize memory into a trusted system, automate repetitive tasks, and create clear, checklist-driven workflows that reduce the mental cost of context-switching between the four core roles: **Strategist**, **Engineer**, **Scientist**, and **Operator**.

---

## **Part 1: The Repository Structure (The Digital Workshop)**

*   `app/`: The **ENGINEER** Hat - The Concierge MVP itself.
*   `docs/`: The **STRATEGIST** Hat - The strategic canon and playbooks.
*   `experiments/`: The **SCIENTIST** Hat - The lab notebook for running the experiment.
*   `scripts/`: The **OPERATOR** Hat - Automation and SOP scripts that provide leverage.
*   `.github/workflows/`: Automated quality control for the workshop itself.

---

## **Part 2: The Workflow (The Operating Cadence)**

This is the repeatable weekly cadence for using the **Execution Toolkit Augmentation Layer**.

**Phase 1: Recruitment**
1.  **Prospecting**: Run `python scripts/prospector.py --keywords "B2B SaaS" "AI"` to generate a CSV of potential leads. Manually review this list and add the best candidates to `experiments/00_RECRUITMENT_PIPELINE.md`.
2.  **Outreach**: Run `python scripts/messenger.py`. This script is an interactive checklist that guides you through a robust, manual workflow for sending personalized outreach emails.
3.  **Onboarding**: Once a team commits, run `python scripts/onboarder.py`. This script is a critical, interactive SOP that walks you through every step of onboarding, from updating your tracking files to sending the welcome email, ensuring a flawless process every time.

**Phase 2: Experiment Execution**
1.  **Prep (10 mins before each session)**: Run `python scripts/session_prep.py --team "Team Name"`. This script provides a manual checklist for session preparation.
2.  **Execute Session (60 mins)**: Follow the checklist in `docs/03_FACILITATOR_PLAYBOOK.md`.
3.  **Post-Session Analysis (15 mins after each session)**:
    *   Save recordings.
    *   Run `python scripts/analyze_compass.py --file /path/to/new.json`.
    *   Update `experiments/01_EXPERIMENT_TRACKING.md` with the output and your qualitative notes.

**Phase 3: System Improvement (Weekly)**
*   **Review and Reflect**: Read through all your notes in `experiments/01_EXPERIMENT_TRACKING.md`.
*   **Improve the System**: Dedicate a few hours to improving your own tools. Can the playbooks be clarified? Can the placeholder scripts be made more robust in the future? This is the **self-correction loop**.

---

This system is designed to be the trusted foundation for the first phase of the Archon project, enabling a single operator to perform at an elite level.

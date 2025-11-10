# **Archon Prime V4 - The Integration Layer**

This repository is the complete, self-contained operating system for a solo founder executing the "Concierge MVP" of the Archon project. It is built on the principles of **leverage, automation, and focus**.

This V4 version represents a major upgrade, introducing an **Integration Layer** that connects the toolkit to external services and automates key workflows, dramatically reducing administrative friction.

---

## **Part 1: The Repository Structure (The Digital Workshop)**

*   `app/`: The **ENGINEER** Hat - The Concierge MVP itself.
*   `docs/`: The **STRATEGIST** Hat - The strategic canon and playbooks.
*   `experiments/`: The **SCIENTIST** Hat - The lab notebook.
    *   `compass_files/`: Centralized storage for all `compass.json` artifacts.
*   `scripts/`: The **OPERATOR** Hat - The V4 automation and integration layer.
*   `tests/`: The formal testing framework for the toolkit.
*   `.github/workflows/`: The CI pipeline that automatically runs `pytest`.

---

## **Part 2: The Workflow (The V4 Operating Cadence)**

This is the new, highly streamlined weekly cadence using the **V4 Integration Layer**.

**Phase 1: Recruitment & Onboarding**
1.  **Prospecting**: Run `python scripts/prospector.py --keywords "B2B SaaS"` to generate and interactively add new leads to your pipeline.
2.  **Outreach**: Run `python scripts/messenger.py` to automatically find new leads and guide you through the "Forced Personalization" outreach workflow.
3.  **Onboarding (Fully Automated)**: Once a team commits, run `python scripts/onboarder.py`. This single command now:
    *   Updates the recruitment pipeline.
    *   Creates the new team entry in the experiment tracking file.
    *   **Automatically schedules all 6 recurring weekly sessions** via the Google Calendar API.

**Phase 2: Experiment Execution**
1.  **Prep (Automated, <1 min)**: Run `python scripts/session_prep.py --team "Alpha"`. This script automatically generates a full session briefing, including the path to the team's last `compass.json` file.
2.  **Execute Session (60 mins)**: Follow the checklist in `docs/03_FACILITATOR_PLAYBOOK.md`. After the session, save the new `compass.json` to `experiments/compass_files/` using the format `alpha_week_1.json`.
3.  **Log Session (Automated, 2 mins)**: Run `python scripts/log_session.py`. This new, powerful tool will prompt you for your notes, automatically analyze the new compass file, and update the experiment tracking file with the new data and an incremented week count.

**Phase 3: System Improvement (Weekly)**
*   **Review and Reflect**: The system now handles the administrative details, freeing you to focus on the insights in `experiments/01_EXPERIMENT_TRACKING.md`.
*   **Improve the System**: Dedicate a few hours to improving your own tools. The self-correction loop is the core of the Archon Prime philosophy.

---

This system is the trusted foundation for the Archon project, enabling a single operator to perform at an elite level.

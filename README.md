# **Archon Prime V2.0**

This repository is the complete, self-contained operating system for a solo founder executing the "Concierge MVP" of the Archon project. It is built on the principles of **leverage, automation, and focus**.

Its purpose is to externalize memory into a trusted system, automate repetitive tasks, and create clear, checklist-driven workflows that reduce the mental cost of context-switching between the four core roles: **Strategist**, **Engineer**, **Scientist**, and **Operator**.

---

## **Part 1: The Repository Structure (The Digital Workshop)**

This is the foundational directory structure. Each directory corresponds to a different "hat" the founder wears.

*   `app/`: The **ENGINEER** Hat - The Concierge MVP itself.
*   `docs/`: The **STRATEGIST** Hat - The strategic canon and playbooks.
*   `experiments/`: The **SCIENTIST** Hat - The lab notebook for running the experiment.
*   `scripts/`: The **OPERATOR** Hat - Automation scripts that provide leverage.
*   `.github/workflows/`: Automated quality control for the workshop itself.

---

## **Part 2: The Workflow (The Operating Cadence)**

This is the simple, repeatable weekly cadence for using the toolkit.

**Monday: The Strategist & Operator**
1.  **Review `experiments/00_RECRUITMENT_PIPELINE.md`**: Identify outreach targets.
2.  **Execute Outreach**: Use the templates in `docs/02_COMMUNICATION_TEMPLATES.md`.
3.  **Plan the Week**: Review upcoming sessions in your calendar.

**Tuesday-Thursday: The Facilitator & Scientist**
1.  **Prep (10 mins before each session)**: Run `python scripts/session_prep.py --team "Team Name"`. This will provide manual prep instructions for now.
2.  **Execute Session (60 mins)**: Follow the checklist in `docs/03_FACILITATOR_PLAYBOOK.md`.
3.  **Post-Session Analysis (15 mins after each session)**:
    *   Save recordings.
    *   Run `python scripts/analyze_compass.py --file /path/to/new.json`.
    *   Update `experiments/01_EXPERIMENT_TRACKING.md` with the output and your qualitative notes.

**Friday: The Engineer & Strategist**
1.  **Review the Data**: Read `experiments/01_EXPERIMENT_TRACKING.md` in its entirety. Look for patterns.
2.  **Improve the System**: Spend 2-3 hours improving your own tools (the scripts, the playbooks, the templates). This is the **self-correction loop**.
3.  **Code (if necessary)**: Make improvements to the `app/` itself based on user feedback.

---

This system is designed to be the trusted foundation for the first phase of the Archon project, enabling a single operator to perform at an elite level.

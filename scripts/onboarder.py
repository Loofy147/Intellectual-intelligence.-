from scripts.utils import read_md_with_yaml, write_md_with_yaml
from scripts.google_calendar import create_mock_calendar_service, create_recurring_events

def main():
    """
    Main execution loop for the V4 onboarder script with automated scheduling.
    """
    print("--- Archon Prime Onboarder V4 ---")

    # --- Step 1: Collect Information ---
    print("\n[Step 1: Collect New Team Information]")
    company_name = input("Enter the Company Name (must match pipeline entry exactly): ").strip()
    team_name = input("Enter the internal Team Name (e.g., 'Alpha', 'Bravo'): ").strip()
    contact_email = input("Enter the Key Contact's Email: ").strip()

    if not all([company_name, team_name, contact_email]):
        print("All fields are required. Exiting.")
        return

    # --- Step 2: Update Recruitment Pipeline ---
    pipeline_file = "experiments/00_RECRUITMENT_PIPELINE.md"
    pipeline_data, pipeline_content = read_md_with_yaml(pipeline_file)

    if not pipeline_data:
        print("Could not read pipeline data. Exiting.")
        return

    prospect = next((p for p in pipeline_data.get('prospects', []) if p.get('company_name') == company_name), None)

    if not prospect:
        print(f"Error: Could not find a company named '{company_name}' in the pipeline. Exiting.")
        return

    prospect['status'] = 'Committed'
    prospect['notes'] = f"Onboarding complete. Assigned to Team {team_name}."

    if write_md_with_yaml(pipeline_file, pipeline_data, pipeline_content):
        print(f"Successfully updated '{company_name}' status to 'Committed' in the pipeline.")

    # --- Step 3: Update Experiment Tracking File ---
    tracking_file = "experiments/01_EXPERIMENT_TRACKING.md"
    tracking_data, tracking_content = read_md_with_yaml(tracking_file)

    if tracking_data is None:
        tracking_data = {'teams': []}

    new_team_entry = {
        "team_name": team_name,
        "company_name": company_name,
        "company_description": "TBD",
        "status": "In Progress",
        "key_contact": f"{prospect.get('contact_person').split(',')[0]}, {contact_email}",
        "weeks_completed": 0
    }

    if not any(t['team_name'].lower() == team_name.lower() for t in tracking_data.get('teams', [])):
        tracking_data.setdefault('teams', []).append(new_team_entry)

        new_notes_section = f"\n---\n### **Team {team_name} ({company_name})**\n\n*   **Week 1:**\n*   **Week 2:**\n*   **Week 3:**\n*   **Week 4:**\n*   **Week 5:**\n*   **Week 6:**\n*   **Adoption Signal:** TBD\n*   **Perceived Value Score:** TBD\n"
        tracking_content += new_notes_section

        if write_md_with_yaml(tracking_file, tracking_data, tracking_content):
            print(f"Successfully added 'Team {team_name}' to the experiment tracking file.")

    # --- Step 4: Automated Scheduling ---
    print("\n[Step 4: Scheduling 6 Weekly Sessions via Google Calendar]")
    calendar_service = create_mock_calendar_service()
    if create_recurring_events(calendar_service, team_name, contact_email):
        print("Successfully scheduled all sessions.")
    else:
        print("An error occurred during scheduling. Please schedule manually.")

    # --- Step 5: Final Confirmation ---
    print("\n--- Onboarding Complete ---")
    print("Please remember to send the welcome email.")
    print("="*50)

if __name__ == "__main__":
    main()

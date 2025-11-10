from scripts.utils import read_md_with_yaml, write_md_with_yaml

def main():
    """
    Main execution loop for the new, robust onboarder script.
    This script automates the full onboarding workflow, including updating
    the recruitment pipeline and experiment tracking files.
    """
    print("--- Archon Prime Onboarder V2 ---")

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

    prospect_found = False
    for p in pipeline_data.get('prospects', []):
        if p.get('company_name') == company_name:
            p['status'] = 'Committed'
            p['notes'] = f"Onboarding complete. Assigned to Team {team_name}."
            prospect_found = True
            break

    if not prospect_found:
        print(f"Error: Could not find a company named '{company_name}' in the pipeline. Exiting.")
        return

    if write_md_with_yaml(pipeline_file, pipeline_data, pipeline_content):
        print(f"Successfully updated '{company_name}' status to 'Committed' in the pipeline.")

    # --- Step 3: Update Experiment Tracking File ---
    tracking_file = "experiments/01_EXPERIMENT_TRACKING.md"
    tracking_data, tracking_content = read_md_with_yaml(tracking_file)

    if tracking_data is None:
        tracking_data = {'teams': []} # Handle case where file is empty or has no YAML

    # Get details from pipeline to populate tracking file
    prospect = next((p for p in pipeline_data['prospects'] if p['company_name'] == company_name), None)

    new_team_entry = {
        "team_name": team_name,
        "company_name": company_name,
        "company_description": "TBD", # Placeholder
        "status": "In Progress",
        "key_contact": f"{prospect.get('contact_person').split(',')[0]}, {contact_email}",
        "weeks_completed": 0
    }

    # Check if team already exists to prevent duplicates
    if not any(t['team_name'].lower() == team_name.lower() for t in tracking_data.get('teams', [])):
        tracking_data.setdefault('teams', []).append(new_team_entry)

        # Also append a new markdown section for notes
        new_notes_section = f"""
---
### **Team {team_name} ({company_name})**

*   **Week 1:**
*   **Week 2:**
*   **Week 3:**
*   **Week 4:**
*   **Week 5:**
*   **Week 6:**
*   **Adoption Signal:** TBD
*   **Perceived Value Score:** TBD
"""
        tracking_content += new_notes_section

        if write_md_with_yaml(tracking_file, tracking_data, tracking_content):
            print(f"Successfully added 'Team {team_name}' to the experiment tracking file.")

    # --- Step 4: Final Confirmation ---
    print("\n--- Onboarding Complete ---")
    print("Please remember to send the welcome email and schedule the first session.")
    print("="*50)

if __name__ == "__main__":
    main()

# onboarder.py - The Onboarding Standard Operating Procedure (SOP)

def main():
    """
    This interactive script serves as a checklist to ensure a flawless and
    consistent onboarding process for every new team.

    It prioritizes data integrity by guiding the operator through manual file
    updates, avoiding the risk of a buggy script corrupting our core records.
    """
    print("="*50)
    print("--- Archon Prime: New Team Onboarding SOP ---")
    print("="*50)

    # --- Step 1: Collect Information ---
    print("\n[Step 1: Collect New Team Information]")
    team_name_raw = input("Enter the official Team Name (e.g., 'Team Alpha'): ").strip()
    company_name = input("Enter the Company Name & One-Liner: ").strip()
    contact_person = input("Enter the Key Contact's Full Name: ").strip()
    contact_email = input("Enter the Key Contact's Email: ").strip()

    team_name = team_name_raw.split()[-1] # Extract 'Alpha' from 'Team Alpha'

    # --- Step 2: Update Recruitment Pipeline ---
    print("\n[Step 2: Update Recruitment Pipeline]")
    print(f"ACTION: Open 'experiments/00_RECRUITMENT_PIPELINE.md'.")
    print(f"        Find '{company_name}' and change their status to 'Onboarded'.")
    input("Press Enter to confirm you have completed this step.")

    # --- Step 3: Update Experiment Tracking File ---
    print("\n[Step 3: Update Experiment Tracking File]")
    print("ACTION: Open 'experiments/01_EXPERIMENT_TRACKING.md'.")
    print("        Copy the template below and paste it in for the new team.")
    print("-" * 20)
    print(f"""### **Team {team_name}**

*   **Company:** {company_name}
*   **Status:** In Progress
*   **Key Contact:** {contact_person}, {contact_email}
*   **Weeks Completed:** 0
*   **Notes:**
    *   Week 1:
    *   Week 2:
    *   Week 3:
    *   Week 4:
    *   Week 5:
    *   Week 6:
*   **Adoption Signal:** TBD
*   **Perceived Value Score:** TBD""")
    print("-" * 20)
    input("Press Enter to confirm you have completed this step.")

    # --- Step 4: Send Welcome Email ---
    print("\n[Step 4: Send the Welcome Email]")
    print("ACTION: Copy the email body below and send it to the Key Contact.")
    print("        The template is also in 'docs/02_COMMUNICATION_TEMPLATES.md'.")
    print("-" * 20)
    print(f"""Subject: Welcome to The Pragmatic Compass Program!

Hi {contact_person.split()[0]},

Welcome! I'm thrilled to have you on board for the 6-week Pragmatic Compass program.

Our goal over the next six weeks is to work together to install a durable, repeatable process for making high-quality strategic decisions at the core of your company.

Here are your next steps:
1.  **The Tool:** Please take a moment to familiarize yourself with the Pragmatic Compass template, which we will be using in our sessions. You can access it here: [Link to app/index.html]
2.  **How it Works:** The tool is 100% client-side. To save your work, use the "Save as JSON" button. To load it in a future session, use the "Load from JSON" button. Please designate one person as the "owner" of your team's JSON file.
3.  **Our First Session:** I've sent a separate calendar invitation for our first session. We will hit the ground running, so please come prepared to discuss the "Three Questions" at a high level.

I'm incredibly excited to begin this journey with you.

Best,

Jules""")
    print("-" * 20)
    input("Press Enter to confirm you have sent the email.")

    print("\n--- Onboarding Complete ---")
    print(f"{company_name} has been successfully onboarded. Well done.")
    print("="*50)

if __name__ == "__main__":
    main()

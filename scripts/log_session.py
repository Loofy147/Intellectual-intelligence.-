from scripts.utils import read_md_with_yaml, write_md_with_yaml
import datetime
import json
import re

def main():
    """
    Main execution loop for the log_session script.
    This tool automates the post-session workflow of logging notes,
    analyzing the compass file, and updating the experiment tracking document.
    """
    print("--- Archon Prime Session Logger V1 ---")

    # --- Step 1: Collect Information ---
    team_name = input("Enter the Team Name (e.g., 'Alpha'): ").strip()
    week_number = input("Enter the Week Number you just completed: ").strip()
    notes = input("Enter your qualitative notes for this session:\n> ").strip()

    compass_filename = f"experiments/compass_files/{team_name.lower()}_week_{week_number}.json"
    print(f"Attempting to read compass file: {compass_filename}")

    if not all([team_name, week_number, notes]):
        print("All fields are required. Exiting.")
        return

    # --- Step 2: Analyze Compass File ---
    try:
        with open(compass_filename, 'r') as f:
            compass_data = json.load(f)
        # A simple analysis: count the number of filled-out sections
        filled_sections = sum(1 for v in compass_data.values() if v.strip())
        analysis = f"Compass analysis: {filled_sections}/{len(compass_data)} sections filled."
    except FileNotFoundError:
        print(f"Warning: Could not find compass file at '{compass_filename}'. Skipping analysis.")
        analysis = "Compass file not found."
    except json.JSONDecodeError:
        print(f"Warning: Could not parse compass file at '{compass_filename}'. Skipping analysis.")
        analysis = "Invalid compass JSON."

    # --- Step 3: Update Experiment Tracking File ---
    tracking_file = "experiments/01_EXPERIMENT_TRACKING.md"
    data, content = read_md_with_yaml(tracking_file)

    if data is None:
        print("Error: Could not read or parse the tracking file. Exiting.")
        return

    # Update YAML data
    team_updated = False
    for team in data.get('teams', []):
        if team.get('team_name', '').lower() == team_name.lower():
            team['weeks_completed'] = int(week_number)
            team_updated = True
            break

    if not team_updated:
        print(f"Error: Could not find 'Team {team_name}' in the tracking file. Exiting.")
        return

    # Update Markdown content
    note_to_add = f"{notes} ({analysis})"
    # Regex to find and replace the correct week's note line
    # It looks for "*   Week X:" and replaces the rest of the line
    note_regex = re.compile(rf"(\*\s+Week\s+{week_number}:).*", re.IGNORECASE)
    new_content, num_replacements = note_regex.subn(rf"\1 {note_to_add}", content)

    if num_replacements == 0:
        print(f"Warning: Could not find the line for 'Week {week_number}' in the notes for Team {team_name}. Appending note manually.")
        # A simple fallback if the regex fails
        content += f"\n*   Week {week_number}: {note_to_add}\n"
    else:
        content = new_content

    # Write the changes back to the file
    if write_md_with_yaml(tracking_file, data, content):
        print(f"\nSuccessfully logged session for Team {team_name}, Week {week_number}.")
        print("Tracking file has been updated.")

    print("\n--- Logging Complete ---")

if __name__ == "__main__":
    main()

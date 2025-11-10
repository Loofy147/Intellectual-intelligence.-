import argparse
from scripts.utils import read_md_with_yaml
import re

def main():
    """
    Main execution loop for the new, robust session_prep script.
    """
    parser = argparse.ArgumentParser(
        description="Generate a pre-session briefing for a facilitation session."
    )
    parser.add_argument(
        "--team",
        type=str,
        required=True,
        help="The name of the team to generate the briefing for (e.g., 'Alpha', 'Bravo').",
    )
    args = parser.parse_args()

    print(f"--- Archon Prime Session Prep V2: Team {args.team} ---")

    tracking_file = "experiments/01_EXPERIMENT_TRACKING.md"
    data, content = read_md_with_yaml(tracking_file)

    if not data or 'teams' not in data:
        print("Error: Could not read valid team data from tracking file.")
        return

    team_data = next((t for t in data['teams'] if t.get('team_name', '').lower() == args.team.lower()), None)

    if not team_data:
        print(f"Error: Could not find data for 'Team {args.team}' in the YAML frontmatter.")
        return

    # Extract data from YAML
    company = team_data.get('company_name', 'N/A')
    weeks_completed = int(team_data.get('weeks_completed', 0))

    # Extract last week's insight from the Markdown content
    last_weeks_insight = "N/A (First Session)"
    # Find the markdown section for the specific team
    team_notes_regex = re.compile(rf"### .*?Team {re.escape(args.team)}.*?\n(.*?)(?=\n---|\Z)", re.DOTALL | re.IGNORECASE)
    notes_match = team_notes_regex.search(content)
    if notes_match:
        notes_section = notes_match.group(1)
        # Find all "Week X: ..." notes that are not placeholders
        weekly_notes = re.findall(r"Week\s\d+:\s*(?!\[Notes for)(.+)", notes_section)
        if weekly_notes:
            last_weeks_insight = weekly_notes[-1].strip()

    facilitator_goal = f"Guide them according to the playbook for Week {weeks_completed + 1}"

    # Print the briefing
    print("="*50)
    print(f"SESSION BRIEFING: Team {args.team} ({company}) - Week {weeks_completed + 1}")
    print("="*50)
    print(f"Last Week's Key Insight: {last_weeks_insight}")
    print(f"Facilitator Goal for Today: {facilitator_goal}")
    print("="*50)

if __name__ == "__main__":
    main()

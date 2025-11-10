# session_prep.py - Placeholder

import argparse

def show_manual_instructions(team_name):
    """
    This is a placeholder script. The automatic parsing logic for the
    experiment tracking file proved to be too brittle.

    Instead, please follow these manual steps for session preparation.
    """

    tracking_file = "experiments/01_EXPERIMENT_TRACKING.md"

    print("="*50)
    print("MANUAL SESSION PREPARATION REQUIRED")
    print("="*50)
    print(f"TEAM: {team_name}")
    print("\nACTION REQUIRED:")
    print(f"1. Open the tracking file: {tracking_file}")
    print(f"2. Review the latest notes for 'Team {team_name}'.")
    print("3. Identify the current week number and facilitator goals.")
    print("4. Ask the team for their latest 'compass.json' file.")
    print("\nThis script will be implemented with a more robust parsing")
    print("method in a future iteration.")
    print("="*50)


if __name__ == "__main__":
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
    show_manual_instructions(args.team)

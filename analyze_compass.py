import json
import argparse

def analyze_compass(file_path):
    """
    Reads a Pragmatic Compass JSON file and prints a formatted summary.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
        return

    print("="*80)
    print("                PRAGMATIC COMPASS ANALYSIS")
    print("="*80)
    print("\n--- The Three Questions ---\n")
    print("1. Non-Obvious Market Dislocation:")
    print(f"   {data.get('q1', 'N/A')}\n")
    print("2. Asymmetric, Defensible Advantage (The Moat):")
    print(f"   {data.get('q2', 'N/A')}\n")
    print("3. Single, Greatest, Non-Technical Risk (The GTM Risk):")
    print(f"   {data.get('q3', 'N/A')}\n")

    print("\n--- The Adversarial Check ---\n")
    print("1. Pre-Mortem Headline:")
    print(f"   {data.get('ac1', 'N/A')}\n")
    print("2. Incumbent's and Platform's Kill Strategy:")
    print(f"   {data.get('ac2', 'N/A')}\n")

    print("\n--- The Lean Experiment ---\n")
    print("1. Single Riskiest Assumption:")
    print(f"   {data.get('le1', 'N/A')}\n")
    print("2. Cheapest, Fastest Way to Test:")
    print(f"   {data.get('le2', 'N/A')}\n")
    print("3. Quantifiable Signal to Prove/Disprove:")
    print(f"   {data.get('le3', 'N/A')}\n")
    print("="*80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze a Pragmatic Compass JSON file."
    )
    parser.add_argument(
        "file_path",
        type=str,
        help="The path to the pragmatic-compass.json file.",
    )
    args = parser.parse_args()
    analyze_compass(args.file_path)

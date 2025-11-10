from scripts.utils import read_md_with_yaml
import webbrowser
import urllib.parse
import re

def get_prospects_from_pipeline():
    """
    Parses the recruitment pipeline YAML to find prospects with the status 'Identified'.
    """
    pipeline_file = "experiments/00_RECRUITMENT_PIPELINE.md"
    data, _ = read_md_with_yaml(pipeline_file)

    if not data or 'prospects' not in data:
        return []

    return [p for p in data['prospects'] if p.get('status') == 'Identified']

def get_email_template():
    """
    Loads the initial recruitment email template.
    """
    template_file = "docs/02_COMMUNICATION_TEMPLATES.md"
    try:
        with open(template_file, 'r') as f:
            content = f.read()
            template_section = re.search(r"## Template 1: Initial Recruitment Outreach \(Email\)(.*?)---", content, re.DOTALL)
            if template_section:
                template_text = template_section.group(1)
                subject = re.search(r"Subject:\s*\**?(.*?)\**?$", template_text, re.MULTILINE).group(1).strip()
                body = template_text.split("Hi [Founder Name],")[1].strip()
                return {"subject": subject, "body": body}
    except FileNotFoundError:
        print(f"Error: Could not find the template file at {template_file}")
    return None

def main():
    """
    Main execution loop for the new, robust messenger script.
    """
    print("--- Archon Prime Messenger V2 ---")
    prospects = get_prospects_from_pipeline()
    template = get_email_template()

    if not prospects:
        print("No prospects with status 'Identified' found in your pipeline.")
        return

    if not template:
        print("Could not load the email template.")
        return

    print(f"Found {len(prospects)} prospect(s) to contact.")

    for prospect in prospects:
        contact_name = prospect['contact_person'].split(',')[0] # Get just the name
        company_name = prospect['company_name']

        print(f"\n--- Preparing email for {contact_name} at {company_name} ---")

        # The "Forced Personalization" Mechanism
        while True:
            personal_line = input("[!] Provide a unique, one-sentence personalized line:\n> ")
            if personal_line.strip():
                break
            print("Personalization cannot be empty.")

        # Construct the email
        subject = template['subject']
        first_name = contact_name.split()[0]
        body = f"Hi {first_name},\n\n{personal_line}\n\n"
        body += template['body'].replace("[Your Name]", "Jules") # Placeholder name

        # Generate mailto link
        encoded_subject = urllib.parse.quote(subject)
        encoded_body = urllib.parse.quote(body)
        mailto_link = f"mailto:?subject={encoded_subject}&body={encoded_body}"

        print("\n--- Email Preview ---")
        print(f"Subject: {subject}")
        print(body)
        print("--------------------")

        action = input("Press 'o' to open in email client, or 's' to skip: ").lower()
        if action == 'o':
            print("Opening in your default email client...")
            # webbrowser.open(mailto_link)
            print("SIMULATED: Would open mailto link.")

if __name__ == "__main__":
    main()

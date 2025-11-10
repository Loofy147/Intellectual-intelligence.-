import os
import argparse
import requests
import csv
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Constants ---
API_BASE_URL = "https://api.companyenrich.com/v1" # Assuming v1 endpoint

def search_companies(keywords, source, limit=20):
    """
    Searches the CompanyEnrich API for companies matching the given keywords.
    """
    api_key = os.getenv("PROSPECTOR_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("Error: PROSPECTOR_API_KEY not found in .env file.")
        print("Please create a .env file and add your API key.")
        return None

    search_endpoint = f"{API_BASE_URL}/companies/search"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # --- ASSUMPTION ---
    # The API documentation lacks the exact request body schema.
    # I am assuming a logical structure based on the text description.
    # This may need to be adjusted.
    payload = {
        "query": {
            "bool": {
                "must": [
                    {"terms": {"tags": keywords}},
                    {"term": {"source": source}}
                ]
            }
        },
        "size": limit
    }

    try:
        response = requests.post(search_endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
        print(f"Response Body: {response.text}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    return None

def write_prospects_to_csv(results):
    """
    Writes the API results to a timestamped CSV file.
    """
    if not results or 'data' not in results or not results['data']:
        print("No results to write.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"prospects_{timestamp}.csv"

    # --- ASSUMPTION ---
    # Assuming the response contains a 'data' list with company objects.
    # The keys ('name', 'domain', 'short_description') are logical assumptions.
    fieldnames = ['CompanyName', 'ContactPerson', 'URL', 'BriefDescription']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for company in results['data']:
            writer.writerow({
                'CompanyName': company.get('name', 'N/A'),
                'ContactPerson': 'N/A', # This API doesn't provide contacts
                'URL': f"https://{company.get('domain', '')}",
                'BriefDescription': company.get('short_description', 'N/A')
            })

    print(f"Successfully wrote {len(results['data'])} prospects to {filename}")
    print("Next Step: Manually review this file and copy the best-fit companies into 'experiments/00_RECRUITMENT_PIPELINE.md'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Search for potential companies using the CompanyEnrich API."
    )
    parser.add_argument(
        "--keywords",
        nargs='+',
        required=True,
        help="A list of keywords/tags to search for (e.g., 'B2B SaaS' 'AI')."
    )
    parser.add_argument(
        "--source",
        type=str,
        default="wellfound",
        help="The source to search from (e.g., 'wellfound', 'linkedin')."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="The maximum number of results to return. Default is 20."
    )

    args = parser.parse_args()

    print(f"Searching for up to {args.limit} companies with keywords: {args.keywords}...")
    results = search_companies(args.keywords, args.source, args.limit)

    if results:
        write_prospects_to_csv(results)

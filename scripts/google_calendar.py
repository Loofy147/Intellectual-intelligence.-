# scripts/google_calendar.py

import datetime

def create_mock_calendar_service():
    """
    A mock function that simulates the creation of a Google Calendar service object.
    In a real implementation, this would handle the OAuth 2.0 flow.
    """
    print("MOCK: Authenticating with Google Calendar API...")
    # In a real implementation, this would return a build() object.
    # We will return a mock object with a predictable structure.
    class MockEvents:
        def insert(self, calendarId, body):
            class MockRequest:
                def execute(self):
                    print(f"MOCK: Creating event: {body['summary']} on {body['start']['dateTime']}")
                    # In a real implementation, this would return the event resource
                    return {"id": "mock_event_id"}
            return MockRequest()

    class MockService:
        def events(self):
            return MockEvents()

    return MockService()


def create_recurring_events(service, team_name, contact_email):
    """
    Creates 6 recurring weekly events for the new team.
    """
    print(f"MOCK: Scheduling 6 weekly sessions for {team_name} with {contact_email}...")

    # In a real implementation, you would calculate the next 6 weeks' dates
    for i in range(1, 7):
        event_body = {
            'summary': f'Archon Prime Strategy Session: Week {i} ({team_name})',
            'description': 'Weekly strategy session for the Concierge MVP program.',
            'start': {
                'dateTime': (datetime.datetime.now() + datetime.timedelta(weeks=i)).isoformat(),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': (datetime.datetime.now() + datetime.timedelta(weeks=i, hours=1)).isoformat(),
                'timeZone': 'UTC',
            },
            'attendees': [
                {'email': contact_email},
                # {'email': 'your_email@example.com'}, # Add the facilitator's email
            ],
        }

        try:
            event = service.events().insert(calendarId='primary', body=event_body).execute()
            print(f"  - Mock Event for Week {i} created.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    return True

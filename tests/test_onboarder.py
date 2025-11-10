import unittest
from unittest.mock import patch
from scripts.onboarder import main

class TestOnboarderV4(unittest.TestCase):

    PIPELINE_DATA = {
        "prospects": [
            {"company_name": "TestCorp", "contact_person": "Jane Doe, CEO", "status": "Contacted"}
        ]
    }
    TRACKING_DATA = {"teams": []}

    @patch("scripts.onboarder.create_recurring_events")
    @patch("scripts.onboarder.create_mock_calendar_service")
    @patch("scripts.onboarder.write_md_with_yaml")
    @patch("scripts.onboarder.read_md_with_yaml")
    @patch("builtins.input", side_effect=["TestCorp", "Alpha", "jane@test.co"])
    def test_onboarding_with_scheduling(self, mock_input, mock_read_yaml, mock_write_yaml, mock_create_service, mock_create_events):
        """Test the V4 onboarding workflow, including the scheduling step."""

        mock_read_yaml.side_effect = [
            (self.PIPELINE_DATA, "# Pipeline"),
            (self.TRACKING_DATA, "# Tracking")
        ]
        mock_create_events.return_value = True # Simulate successful scheduling

        main()

        # Check that the core file-writing functions were called
        self.assertEqual(mock_write_yaml.call_count, 2)

        # Check that the scheduling functions were called
        self.assertTrue(mock_create_service.called)
        self.assertTrue(mock_create_events.called)

        # Verify the correct arguments were passed to the scheduling function
        mock_create_events.assert_called_with(unittest.mock.ANY, "Alpha", "jane@test.co")

if __name__ == "__main__":
    unittest.main()

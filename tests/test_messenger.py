import unittest
from unittest.mock import patch
from scripts.messenger import get_prospects_from_pipeline, main

class TestMessengerV2(unittest.TestCase):

    @patch("scripts.messenger.read_md_with_yaml")
    def test_get_prospects_from_pipeline(self, mock_read_yaml):
        """Test that prospects are correctly filtered from the YAML data."""
        mock_read_yaml.return_value = ({
            "prospects": [
                {"company_name": "TestCorp 1", "status": "Identified"},
                {"company_name": "TestCorp 2", "status": "Contacted"},
                {"company_name": "TestCorp 3", "status": "Identified"},
            ]
        }, "Markdown content")

        prospects = get_prospects_from_pipeline()
        self.assertEqual(len(prospects), 2)
        self.assertEqual(prospects[0]['company_name'], 'TestCorp 1')

    @patch("scripts.messenger.get_email_template", return_value={"subject": "Sub", "body": "Body"})
    @patch("scripts.messenger.get_prospects_from_pipeline")
    @patch("builtins.input", side_effect=["Personal line.", "s"])
    def test_main_loop(self, mock_input, mock_get_prospects, mock_get_template):
        """Test the main loop runs correctly."""
        mock_get_prospects.return_value = [
            {"company_name": "TestCorp", "contact_person": "Jane Doe, CEO"}
        ]
        main()
        self.assertEqual(mock_input.call_count, 2)

if __name__ == "__main__":
    unittest.main()

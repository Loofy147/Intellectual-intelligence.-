import unittest
from unittest.mock import patch, mock_open
from scripts.log_session import main

class TestLogSessionV1(unittest.TestCase):

    TRACKING_DATA_INITIAL = {
        "teams": [
            {"team_name": "Alpha", "weeks_completed": 1}
        ]
    }
    TRACKING_CONTENT_INITIAL = """---
# YAML above
---
### **Team Alpha (InnovateCorp AI)**

*   Week 1: Old note.
*   Week 2: [Notes for Week 2]
"""
    COMPASS_DATA = '{"q1": "Answered", "q2": ""}' # 1 of 2 sections filled

    @patch("scripts.log_session.write_md_with_yaml")
    @patch("scripts.log_session.read_md_with_yaml")
    @patch("builtins.open", new_callable=mock_open, read_data=COMPASS_DATA)
    @patch("builtins.input", side_effect=["Alpha", "2", "New session notes."])
    def test_log_session_workflow(self, mock_input, mock_file_open, mock_read_yaml, mock_write_yaml):
        """Test the full, successful workflow of the log_session script."""

        mock_read_yaml.return_value = (self.TRACKING_DATA_INITIAL, self.TRACKING_CONTENT_INITIAL)

        main()

        self.assertTrue(mock_write_yaml.called)

        # Inspect the data that was passed to the write function
        write_args = mock_write_yaml.call_args.args
        written_data = write_args[1]
        written_content = write_args[2]

        # Check YAML updates
        self.assertEqual(written_data['teams'][0]['weeks_completed'], 2)

        # Check Markdown content updates
        self.assertIn("*   Week 2: New session notes. (Compass analysis: 1/2 sections filled.)", written_content)
        self.assertIn("*   Week 1: Old note.", written_content) # Ensure old notes are preserved


if __name__ == "__main__":
    unittest.main()

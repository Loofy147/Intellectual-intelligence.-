import unittest
from unittest.mock import patch, mock_open
from scripts import session_prep

class TestSessionPrepV4(unittest.TestCase):

    YAML_DATA = {
        "teams": [
            {"team_name": "Alpha", "company_name": "TestCorp", "weeks_completed": 1}
        ]
    }
    MD_CONTENT = """
---
### **Team Alpha (TestCorp)**
*   Week 1: A real note.
"""

    @patch("os.path.exists", return_value=True)
    @patch("argparse.ArgumentParser.parse_args")
    @patch("scripts.session_prep.read_md_with_yaml")
    @patch("builtins.print")
    def test_session_prep_with_file_retrieval(self, mock_print, mock_read_yaml, mock_parse_args, mock_path_exists):
        """Test the V4 session prep briefing with automated file retrieval."""
        mock_parse_args.return_value.team = "Alpha"
        mock_read_yaml.return_value = (self.YAML_DATA, self.MD_CONTENT)

        session_prep.main()

        printed_output = "\n".join([call.args[0] for call in mock_print.call_args_list])

        # Assert that the script found the file and included it in the briefing
        expected_path = "experiments/compass_files/alpha_week_1.json"
        self.assertIn(f"Last Compass File: {expected_path}", printed_output)
        self.assertIn("Last Week's Key Insight: A real note.", printed_output)


if __name__ == "__main__":
    unittest.main()

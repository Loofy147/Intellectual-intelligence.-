import os
import unittest
from unittest.mock import patch, mock_open
import csv

from scripts.prospector import add_to_pipeline_prompt

class TestProspector(unittest.TestCase):

    def test_add_to_pipeline_prompt_adds_prospects(self):
        """
        Verify that add_to_pipeline_prompt correctly reads a CSV,
        prompts the user, and writes the selected prospect to the
        pipeline markdown file.
        """
        # 1. Setup mock data
        mock_csv_data = (
            "CompanyName,ContactPerson,URL,BriefDescription\n"
            "TestCorp,John Doe,https://test.com,A test company"
        )
        mock_md_data = {
            'prospects': []
        }
        mock_md_content = "\n## Some Markdown Content"

        # 2. Patch the built-in 'open' function, 'input', and the file utilities
        with patch('builtins.open', mock_open(read_data=mock_csv_data)) as mocked_file, \
             patch('builtins.input', side_effect=['y', '1']), \
             patch('scripts.prospector.read_md_with_yaml', return_value=(mock_md_data, mock_md_content)) as mock_read, \
             patch('scripts.prospector.write_md_with_yaml', return_value=True) as mock_write:

            # 3. Call the function
            add_to_pipeline_prompt("dummy.csv")

            # 4. Assertions
            # It should ask the user to add prospects
            self.assertEqual(mocked_file.call_count, 1) # Should open the CSV

            # It should read the pipeline file
            mock_read.assert_called_once_with("experiments/00_RECRUITMENT_PIPELINE.md")

            # It should write the updated data to the pipeline file
            mock_write.assert_called_once()

            # Check the data that was written
            written_data = mock_write.call_args[0][1]
            self.assertEqual(len(written_data['prospects']), 1)
            self.assertEqual(written_data['prospects'][0]['company_name'], "TestCorp")
            self.assertEqual(written_data['prospects'][0]['status'], "Identified")

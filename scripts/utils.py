import yaml
import re

def read_md_with_yaml(filepath):
    """
    Reads a markdown file with YAML frontmatter, separating the two.
    Returns a tuple of (data, content).
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        # Regex to find the YAML frontmatter
        yaml_match = re.search(r'^---\s*\n(.*?\n?)^---\s*$\n?(.*)', text, re.DOTALL | re.MULTILINE)

        if yaml_match:
            yaml_str = yaml_match.group(1)
            content = yaml_match.group(2)
            data = yaml.safe_load(yaml_str)
            return data, content
        else:
            # If no YAML, return empty data and the full text as content
            return None, text

    except FileNotFoundError:
        print(f"Error: Could not find the file at {filepath}")
        return None, None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {filepath}: {e}")
        return None, None

def write_md_with_yaml(filepath, data, content):
    """
    Writes a dictionary to a YAML frontmatter section of a markdown file.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            yaml_str = yaml.dump(data, default_flow_style=False)
            f.write("---\n")
            f.write(yaml_str)
            f.write("---\n")
            f.write(content)
        return True
    except IOError as e:
        print(f"Error writing to file {filepath}: {e}")
        return False

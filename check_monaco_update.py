#!/usr/bin/env python3
"""
Check for Monaco Editor updates and update the update_editor.sh script
"""

import json
import os
import re
import sys
import urllib.request


def get_latest_monaco_version():
    url = "https://registry.npmjs.org/monaco-editor/"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    return data['dist-tags']['latest']


def get_current_version_from_script(script_path='update_editor.sh'):
    with open(script_path, 'r') as f:
        content = f.read()
    
    version_match = re.search(r'MONACO_VERSION=(\d+\.\d+)', content)
    patch_match = re.search(r'MONACO_VERSION_PATCH=(\d+)', content)
    
    if version_match and patch_match:
        return f"{version_match.group(1)}.{patch_match.group(1)}", content
    return "0.0.0", content


def update_script_version(content, new_version):
    parts = new_version.split('.')
    new_major_minor = f"{parts[0]}.{parts[1]}"
    new_patch = parts[2] if len(parts) > 2 else "0"
    
    content = re.sub(r'MONACO_VERSION=\d+\.\d+', f'MONACO_VERSION={new_major_minor}', content)
    content = re.sub(r'MONACO_VERSION_PATCH=\d+', f'MONACO_VERSION_PATCH={new_patch}', content)
    
    return content


def set_github_output(key, value):
    """Set GitHub Actions output"""
    github_output = os.environ.get('GITHUB_OUTPUT')
    if github_output:
        with open(github_output, 'a') as f:
            f.write(f"{key}={value}\n")


def main():
    try:
        # Get versions
        latest_version = get_latest_monaco_version()
        print(f"Latest Monaco Editor version: {latest_version}")
        
        current_version, script_content = get_current_version_from_script()
        print(f"Current version: {current_version}")
        
        # Compare and update if needed
        if latest_version != current_version:
            print(f"Update needed: {current_version} -> {latest_version}")
            
            # Update the script
            updated_content = update_script_version(script_content, latest_version)
            with open('update_editor.sh', 'w') as f:
                f.write(updated_content)
            
            # Set GitHub Actions outputs
            set_github_output("updated", "true")
            set_github_output("new_version", latest_version)
        else:
            print("Already up to date")
            set_github_output("updated", "false")
        
        return 0
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
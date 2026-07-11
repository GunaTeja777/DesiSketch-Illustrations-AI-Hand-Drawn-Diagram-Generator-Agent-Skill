#!/usr/bin/env python3
import os
import re
import sys
import yaml

def check_file_exists(filepath):
    if not os.path.isfile(filepath):
        print(f"[-] ERROR: File does not exist: {filepath}")
        return False
    print(f"[+] OK: Found file: {filepath}")
    return True

def validate_skill_file(skill_path):
    print("--- Validating SKILL.md ---")
    if not check_file_exists(skill_path):
        return False

    with open(skill_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verify YAML frontmatter
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        print("[-] ERROR: SKILL.md does not contain valid YAML frontmatter (needs leading/trailing ---).")
        return False

    frontmatter_text = match.group(1)
    body_text = match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except Exception as e:
        print(f"[-] ERROR: Failed to parse YAML frontmatter: {e}")
        return False

    # Check required frontmatter keys
    required_keys = ['name', 'description']
    for key in required_keys:
        if key not in frontmatter:
            print(f"[-] ERROR: Frontmatter is missing key: '{key}'")
            return False
        if not frontmatter[key] or not str(frontmatter[key]).strip():
            print(f"[-] ERROR: Frontmatter key '{key}' has an empty or invalid value.")
            return False

    print(f"[+] OK: Skill Name: {frontmatter['name']}")
    print(f"[+] OK: Description length: {len(frontmatter['description'])} characters")

    # Scan body for referenced manual files
    references_dir = os.path.join(os.path.dirname(skill_path), "references")
    referenced_files = re.findall(r"`references/([^`\n]+)`", body_text)
    
    if not referenced_files:
        print("[-] WARNING: No reference manual files are referenced in the SKILL.md body text.")
    
    success = True
    for ref_file in referenced_files:
        ref_path = os.path.join(references_dir, ref_file)
        if not check_file_exists(ref_path):
            success = False

    return success

def validate_readme_images(readme_path, base_dir):
    print("--- Validating README.md Image References ---")
    if not check_file_exists(readme_path):
        return False

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find markdown images like ![Alt Text](examples/images/...)
    image_refs = re.findall(r"!\[.*?\]\((.*?)\)", content)
    if not image_refs:
        print("[+] OK: No image references found in README.")
        return True

    success = True
    for img in image_refs:
        # Ignore external HTTP links
        if img.startswith("http://") or img.startswith("https://"):
            continue
        
        # Clean relative link formatting (e.g. removing prefix file:///)
        clean_img = img.replace("file:///", "").strip()
        img_path = os.path.join(base_dir, clean_img)
        if not check_file_exists(img_path):
            success = False

    return success

def main():
    # Root of the repo is parent of tests/
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    skill_path = os.path.join(base_dir, "desisketch-illustrations", "SKILL.md")
    readme_path = os.path.join(base_dir, "README.md")

    skill_ok = validate_skill_file(skill_path)
    readme_ok = validate_readme_images(readme_path, base_dir)

    print("--- Results ---")
    if skill_ok and readme_ok:
        print("[+] SUCCESS: Skill bundle is valid and all dependencies exist!")
        sys.exit(0)
    else:
        print("[-] FAILED: Missing dependencies or invalid configuration detected.")
        sys.exit(1)

if __name__ == "__main__":
    main()

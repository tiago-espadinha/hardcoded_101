"""
Demonstrates re (regex) in Python.
Covers: compile, match, search, findall, groups, substitution
"""
import re

def main():
    text = "Contact us at support@example.com or sales@test.org"
    email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"

    # findall
    emails = re.findall(email_pattern, text)
    print(f"Emails: {emails}")

    # search and groups
    log = "2022-01-31 ERROR System failed"
    match = re.search(r"(\d{4}-\d{2}-\d{2}) (\w+) (.+)", log)
    if match:
        print(f"Date: {match.group(1)}, Level: {match.group(2)}, Msg: {match.group(3)}")

    # substitution
    redacted = re.sub(email_pattern, "[REDACTED]", text)
    print(f"Redacted: {redacted}")

if __name__ == "__main__":
    main()

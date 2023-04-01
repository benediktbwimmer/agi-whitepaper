# python_api.py
#
# Central control unit for the AGI manifest.
# Provides smart ways to update the README and extract data from it.


import os
from readme_utils import update_readme

README_PATH = "README.md"

def read_readme():
    with open(README_PATH, "r") as file:
        return file.read()

def write_readme(content):
    with open(README_PATH, "w") as file:
        file.write(content)

def main():
    content = read_readme()
    updated_content = update_readme(content)
    write_readme(updated_content)

if __name__ == "__main__":
    main()


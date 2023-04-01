import os

class READMEUtils:

    def __init__(self):
        self.readme_path = "agi-whitepapers/README.md"
        self.sections = [
            "Introduction",
            "Process Overview",
            "Sections",
            "Conclusion",
            "Contact Information",
            "Changelog",
            "Potential Applications and Benefits",
            "Limitations of GPT-4 for Software Engineering",
            "Ways that AI can Help Humans Understand the Rapidly Evolving World Around Them Better",
            "GPT-4 Conversation",
            "Fair Decision-Making",
            "README.md as Central Brain",
            "LLM Principles and Capabilities",
            "Python API Plan",
        ]

    def create_section(self, section_title):
        with open(self.readme_path, "a") as readme_file:
            readme_file.write(f"## {section_title}\n\n")

    def add_content(self, section_title, content):
        with open(self.readme_path, "a") as readme_file:
            readme_file.write(f"{content}\n\n")

    def update_plan(self, section_title, progress):
        with open(self.readme_path, "r") as readme_file:
            lines = readme_file.readlines()

        for i, line in enumerate(lines):
            if f"## {section_title}" in line:
                lines.insert(i + 1, f"{progress}\n\n")
                break

        with open(self.readme_path, "w") as readme_file:
            readme_file.writelines(lines)

    def mark_plan_as_done(self, section_title):
        with open(self.readme_path, "r") as readme_file:
            lines = readme_file.readlines()

        for i, line in enumerate(lines):
            if f"## {section_title}" in line:
                lines[i] = f"## {section_title} (Done)\n"
                break

        with open(self.readme_path, "w") as readme_file:
            readme_file.writelines(lines)


if __name__ == "__main__":
    utils = READMEUtils()

    # Example usage:
    utils.create_section("New Section")
    utils.add_content("New Section", "This is the content of the new section.")
    utils.update_plan("New Section", "Progress: 50%")
    utils.mark_plan_as_done("New Section")

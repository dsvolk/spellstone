import frontmatter


class Section:
    def __init__(self, title, level):
        self.title = title
        self.level = level
        self.content = []
        self.subsections = []

    def add_content(self, content):
        self.content.append(content)

    def add_subsection(self, subsection):
        self.subsections.append(subsection)

    def __repr__(self):
        return (
            f"Section(title={self.title}, level={self.level}, content={self.content}, subsections={self.subsections})"
        )


def parse_markdown(file_path):
    root = Section(title="root", level=0)
    current_section = root

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                # Count the level of the section
                level = len(line.split(" ")[0])
                title = line[level + 1 :].strip()

                # Create a new section
                new_section = Section(title=title, level=level)

                # Find the correct parent for the new section
                while current_section.level >= level:
                    current_section = current_section.parent
                current_section.add_subsection(new_section)

                # Update current section
                new_section.parent = current_section
                current_section = new_section
            else:
                # Add line to the content of the current section
                current_section.add_content(line)

    return root


def parse_note(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        post = frontmatter.load(f)

    metadata = post.metadata
    content = post.content

    sections = parse_markdown(file_path)

    return metadata, content, sections

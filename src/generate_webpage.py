import os
from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    if lines[0].startswith("# "):
        return lines[0].strip("#").strip()
    else:
        raise Exception("The first line is not a header")
    
def generate_page(from_path, template_path, dest_path):
    from_path_copy = open_file(from_path)
    template_path_copy = open_file(template_path)
    html_node = markdown_to_html_node(from_path_copy)
    html_str = html_node.to_html()
    title = extract_title(from_path_copy)
    template_path_copy = template_path_copy.replace("{{ Title }}", title)
    template_path_copy = template_path_copy.replace("{{ Content }}", html_str)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(template_path_copy)

def open_file(path):
    file = open(path)
    output = file.read()
    file.close
    return output
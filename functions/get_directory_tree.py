import os
from google.genai import types

IGNORE_DIRS = {
    ".venv",
    "__pycache__",
    ".git",
    "node_modules",
    ".env",
    ".gitignore",
    ".python-version"
}

max_depth = 3

def build_tree(directory=".", current_depth=0, spaces=""):
    if current_depth > max_depth:
        return ""

    temp = os.listdir(directory)
    contents = [
        os.path.join(directory, x)
        for x in temp
        if x not in IGNORE_DIRS
    ]

    if not contents:
        return ""

    tree = ""

    for i, item in enumerate(contents):
        is_last = i == len(contents) - 1

        prefix = "└──" if is_last else "├──"

        name = os.path.basename(item)

        if os.path.isdir(item):
            tree += f"{spaces}{prefix}{name}/\n"

            child_spaces = spaces + "    "

            subtree = build_tree(
                item,
                current_depth + 1,
                child_spaces
            )

            if subtree:
                tree += subtree
        else:
            tree += f"{spaces}{prefix}{name}\n"

    return tree



    
def get_directory_tree(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(
        os.path.join(working_directory, directory)
    )

    if not abs_directory.startswith(abs_working_dir):
        return f'Error: "{directory}" is not in the working directory'

    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'

    return (
        os.path.basename(abs_directory)
        + "/\n"
        + build_tree(abs_directory)
    )

schema_get_directory_tree = types.FunctionDeclaration(
    name="get_directory_tree",
    description=(
        "Displays a directory tree structure relative to the working directory. "
        "Useful for understanding project hierarchy before reading or modifying files. "
        "Ignores common noise directories such as .venv, .git, node_modules and __pycache__."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files and folders from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
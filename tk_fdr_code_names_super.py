import os

def list_directory(path, level=0, output_file=None, exclude_files=None, list_content=False):
    ignored_folders = {
        '.venv', 'venv', 'env', '.idea', '.git', 'node_modules', '__pycache__',
        'dist', 'build', '.DS_Store', '.vscode', 'target', 'out',
        '.pytest_cache', '.mypy_cache', 'logs', 'coverage',
    }

    exclude_files = exclude_files or []

    items = sorted(os.listdir(path))

    for item in items:
        full_path = os.path.join(path, item)

        if item.startswith('.') or item in exclude_files:
            continue

        if os.path.isdir(full_path) and any(ignored in full_path for ignored in ignored_folders):
            continue

        if os.path.isfile(full_path):
            output_file = write_to_output(output_file, f"{'  ' * level}|-- {item}\n")

            if list_content and item.endswith(('.py', '.js', '.java', '.c', '.cpp', '.h', '.ipynb', '.html', '.css', '.ts', '.tsx', '.scss', '.sass', '.vue')):
                output_file = write_to_output(output_file, f"{'  ' * (level + 1)}Content:\n")
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        output_file = write_to_output(output_file, f"{'  ' * (level + 2)}{line}")

        elif os.path.isdir(full_path):
            output_file = write_to_output(output_file, f"{'  ' * level}|-- {item}/\n")
            output_file = list_directory(full_path, level + 1, output_file, exclude_files, list_content)

    return output_file

def write_to_output(output_file, content):
    max_file_size = 24000

    if output_file and output_file.tell() + len(content) > max_file_size:
        output_file.close()

        base_name = os.path.splitext(output_file.name)[0]
        extension = os.path.splitext(output_file.name)[1]

        n = 1
        new_file_name = f"{base_name}_{n}{extension}"
        while os.path.exists(new_file_name):
            n += 1
            new_file_name = f"{base_name}_{n}{extension}"

        output_file = open(new_file_name, 'w', encoding='utf-8')

    output_file.write(content)
    return output_file

def generate_listing(directory_path):
    exclude_files = ['directory_listing.txt', 'tree.txt', os.path.basename(__file__)]
    output_file_path = 'directory_listing.txt'
    output_file = open(output_file_path, 'w', encoding='utf-8')

    list_directory(directory_path, output_file=output_file, exclude_files=exclude_files)
    output_file.write("\n\nFile contents:\n\n")
    list_directory(directory_path, output_file=output_file, exclude_files=exclude_files, list_content=True)
    output_file.close()

def generate_tree(directory_path):
    current_file_name = os.path.basename(__file__)
    exclude_files = [
        'directory_listing.txt', 
        'directory_listing_1.txt', 
        'directory_listing_1_1.txt',
        'directory_listing_1_1_1.txt',
        'directory_listing_1_1_1_1.txt',
        'directory_listing_1_1_1_1_1.txt',
	'tree.txt',  
        current_file_name
    ]
    with open('tree.txt', 'w', encoding='utf-8') as tree_file:
        write_tree(directory_path, tree_file, exclude_files)

def write_tree(directory_path, tree_file, exclude_files, level=0):
    ignored_folders = {
        '.venv', 'venv', 'env', '.idea', '.git', 'node_modules', '__pycache__',
        'dist', 'build', '.DS_Store', '.vscode', 'target', 'out',
        '.pytest_cache', '.mypy_cache', 'logs', 'coverage',
    }

    items = sorted(os.listdir(directory_path))

    for item in items:
        full_path = os.path.join(directory_path, item)

        if item.startswith('.') or item in exclude_files:
            continue

        if os.path.isdir(full_path) and item in ignored_folders:
            continue

        tree_file.write(f"{'  ' * level}|-- {item}\n")

        if os.path.isdir(full_path):
            write_tree(full_path, tree_file, exclude_files, level + 1)

directory_path = './'  # Caminho do diretório a ser listado
generate_listing(directory_path)
generate_tree(directory_path)

print("The directory listing and tree files have been created.")

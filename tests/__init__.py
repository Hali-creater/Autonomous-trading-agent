init_file_path = os.path.join(tests_dir, "__init__.py")
if not os.path.exists(init_file_path):
    with open(init_file_path, "w") as f:
        pass # Create an empty __init__.py file
    print(f"Created {init_file_path}")
else:
    print(f"{init_file_path} already exists.")

# Add the project directory to the Python path to allow importing modules
# This is a common practice for testing modules within a project structure
if project_name not in sys.path:
    sys.path.insert(0, project_name)
    print(f"Added {project_name} to sys.path")

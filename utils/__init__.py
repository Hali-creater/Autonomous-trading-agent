utils_init_path = os.path.join(utils_dir, "__init__.py")
if not os.path.exists(utils_init_path):
    with open(utils_init_path, "w") as f:
        f.write("# utils module __init__.py\n")
        # Add imports for any utility functions defined later
    print(f"Created {utils_init_path}")
else:
    print(f"{utils_init_path} already exists.")


print("Created config/ and utils/ directories and their __init__.py files.")

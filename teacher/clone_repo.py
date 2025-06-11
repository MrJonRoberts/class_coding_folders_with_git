#!/usr/bin/env python3
import subprocess
import os
import sys
# Inherit your normal env, but turn off SSL verification for Git
GIT_ENV = os.environ.copy()
GIT_ENV["GIT_SSL_NO_VERIFY"] = "true"
REPO_URL = "https://github.com/MrJonRoberts/class_repo_test.git"  # replace with your repo URL

def clone_branch(repo_url, branch_name):
    """
    Clone the given repository at the specified branch into a directory named after the branch.
    """
    target_dir = branch_name
    if os.path.exists(target_dir):
        print(f"Directory '{target_dir}' already exists. Skipping clone.")
    else:
        print(f"Cloning branch '{branch_name}' into '{target_dir}'…")
        subprocess.run(
            ["git", "clone", "--branch", branch_name, "--single-branch", repo_url, target_dir],
            check=True,
            env=GIT_ENV
        )
        print("Clone complete.")

if __name__ == "__main__":

    branch = input("Enter your id provided: (eg er31111)")
    if branch == "":
        branch = "fh31450"



    try:
        clone_branch(REPO_URL, branch)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

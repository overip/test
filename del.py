import subprocess

#subprocess.call(["cd", "test"])

subprocess.call(["git", "add", "--all"])

subprocess.call(["git", "commit", "-m", "test_message"])

subprocess.call(["git", "push"])

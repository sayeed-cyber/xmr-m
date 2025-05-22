import os
import platform
import subprocess
import stat
import sys

def run_unix_executable(file_path):
    current_platform = platform.system()

    if current_platform not in ["Linux", "Darwin"]:
        print(f"Cannot run Unix executable on {current_platform}.")
        return

    if not os.path.isfile(file_path):
        print(f"File does not exist: {file_path}")
        return

    # Ensure it's executable
    st = os.stat(file_path)
    if not st.st_mode & stat.S_IXUSR:
        print("Making file executable...")
        os.chmod(file_path, st.st_mode | stat.S_IXUSR)

    try:
        print(f"Running {file_path}...")
        result = subprocess.run([file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Output:")
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print("Error running file:")
        print(e.stderr.decode())

# Example usage
if __name__ == "__main__":
    path_to_executable = "./xmrig"  # Change this to your path
    run_unix_executable(path_to_executable)
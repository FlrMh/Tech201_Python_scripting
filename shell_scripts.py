import os
import subprocess

# Python does not actually run shell commands (terminal commands). Python can run files that then run the shell script.

script_dir = os.path.dirname(__file__) # stores the path to the current file

script_absolute_path = os.path.join(script_dir, "script.sh")

subprocess.call(['.sh', script_absolute_path])
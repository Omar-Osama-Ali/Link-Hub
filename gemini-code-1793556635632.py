# Let's inspect the files in the current directory and subdirectories to see the latest codebase
import os

print("Current directory:", os.getcwd())
print("Directory contents:", os.listdir('.'))

for root, dirs, files in os.walk('.'):
    for file in files:
        print(os.path.join(root, file))
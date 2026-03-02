import glob
# 1. Importing the glob module
# 2. Using glob to find all .txt files in the current directory
txt_files = glob.glob("*.txt")
print("Found .txt files:", txt_files)
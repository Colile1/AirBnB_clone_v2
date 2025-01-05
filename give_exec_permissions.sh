#!/bin/bash

# Check if a directory is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Assign the directory to a variable
DIR="$1"

# Check if the provided argument is a directory
if [ ! -d "$DIR" ]; then
  echo "Error: $DIR is not a directory."
  exit 1
fi

# Check if the directory is a Git repository
if ! git -C "$DIR" rev-parse --git-dir > /dev/null 2>&1; then
  echo "Error: $DIR is not a Git repository."
  exit 1
fi

# Find all files in the directory and subdirectories and give them execute permissions
find "$DIR" -type f -exec chmod +x {} \;

# Stage all changes in the Git repository
git -C "$DIR" add .

# Commit the changes with a message
git -C "$DIR" commit -m "updated permissions +x"

# Push the changes to the remote repository (optional)
git -C "$DIR" push

echo "Execute permissions have been granted to all files in $DIR and its subdirectories."
echo "Changes have been committed to the Git repository with the message: 'updated permissions +x'."

#!/bin/bash

# Get the current day of the month
day=$(date +%d)

# Create a commit message with the current day
commit_message="🎄 Completed day $day"

# Add all changes and commit with the generated message
git add .
git commit -m "$commit_message"

# Print a message indicating the commit is completed
echo "Changes committed with message: $commit_message"

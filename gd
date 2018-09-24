#!/bin/bash

# Check if the date argument was provided
if [ -z "$1" ]; then
    echo "Error: Missing date. Usage: $(basename $0) 'DD/MM/YYYY'"
    exit 1
fi

# Generate a random hour, minute, and second
RANDOM_HOUR=$(printf "%02d" $(( $RANDOM % 24 )))
RANDOM_MINUTE=$(printf "%02d" $(( $RANDOM % 60 )))
RANDOM_SECOND=$(printf "%02d" $(( $RANDOM % 60 )))

# Convert the date format from 'DD/MM/YYYY' to the 'YYYY-MM-DD' format that Git expects.
# Also, add the random time.
FORMATTED_DATE="$(awk -F'/' '{print $3"-"$2"-"$1" "}' <<< $1)${RANDOM_HOUR}:${RANDOM_MINUTE}:${RANDOM_SECOND}"

# Setting the random date for GIT_COMMITTER_DATE and GIT_AUTHOR_DATE
export GIT_COMMITTER_DATE="$FORMATTED_DATE"
export GIT_AUTHOR_DATE="$FORMATTED_DATE"

# Adding all changes to the staging area 
git add .

# Committing with the custom date and random time
git commit -m "Commit on $FORMATTED_DATE"

# Pushing the commit to the remote repository
git push

# Unsetting the variables so they don't affect future commits
unset GIT_COMMITTER_DATE
unset GIT_AUTHOR_DATE

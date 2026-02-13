#!/bin/bash

# Define the zip filename
WEEK=$1
ZIP_FILE="$WEEK".zip

# Basic usage check
if [ -z "$WEEK" ]; then
    echo "Usage:   $0 <week-folder>"
    echo "Example: $0 week1"
  exit 1
fi

echo "Zipping all 'assignments' subdirectories in: $WEEK"

rm -f "$ZIP_FILE"

find "$WEEK" -type d -name assignments -exec \
  zip -r "$ZIP_FILE" "{}" -x '*/__pycache__/*' '*.pyc' \
\;

## If this fails use:
# zip -r $ZIP_FILE ./$WEEK

if [ -f "$ZIP_FILE" ] && [ "$(stat -c %s -- "$ZIP_FILE")" -gt 10000000 ]; then
  echo "The '$ZIP_FILE' is larger than 10MB, see if you can remove some files from '$WEEK' that are not needed for grading and remake this file."
fi

if [ -f "$ZIP_FILE" ]; then
  echo "file size: $(du -h "$ZIP_FILE" | cut -f1)"
  echo "Submit file: $ZIP_FILE"
fi

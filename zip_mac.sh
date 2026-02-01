#!/bin/bash

WEEK="$1"
ZIP_FILE="${WEEK}.zip"

if [ -z "$WEEK" ]; then
  echo "Usage:   $0 <week-folder>"
  echo "Example: $0 week1"
  exit 1
fi

echo "Zipping all 'assignments' subdirectories in: $WEEK"

rm -f "$ZIP_FILE"

find "$WEEK" -type d -name assignments -exec \
  zip -r "$ZIP_FILE" "{}" \
    -x '*/__pycache__/*' '*.pyc' '*.DS_Store' \
    \;

## If this fails use:
# zip -r "$ZIP_FILE" "./$WEEK" -x "*.DS_Store"

# macOS stat: -f %z prints file size in bytes
if [ -f "$ZIP_FILE" ] && [ "$(stat -f %z -- "$ZIP_FILE")" -gt 5000000 ]; then
  echo "The '$ZIP_FILE' is larger than 5MB, see if you can remove some files from '$WEEK' that are not needed for grading and remake this file."
fi

if [ -f "$ZIP_FILE" ]; then
  echo "file size: $(du -h "$ZIP_FILE" | cut -f1)"
  echo "Submit file: $ZIP_FILE"
fi


#!/bin/bash

# Define the zip filename
ZIP_FILE="softeng.zip"

# Run the zip command, excluding .DS_Store files
zip -r "$ZIP_FILE" ./

echo "Zipped all files into $ZIP_FILE"

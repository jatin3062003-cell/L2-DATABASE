#!/bin/bash

# Define the output file
output_file="combined_source_code.txt"

# Clear the output file if it exists
> "$output_file"

# Find all .py files, excluding the output file itself and hidden directories like .venv
# and append their content to the output file
find . -type f -name "*.py" -not -name "$output_file" -not -path "*/.*" | while read -r file; do
    echo "----------------------------------------" >> "$output_file"
    echo "FILE: $file" >> "$output_file"
    echo "----------------------------------------" >> "$output_file"
    cat "$file" >> "$output_file"
    echo -e "\n" >> "$output_file"
done

echo "All source files have been merged into $output_file"
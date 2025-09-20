#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys

# Allowed status codes
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

# Metrics storage
total_size = 0
status_counts = {code: 0 for code in valid_codes}

def print_stats():
    """Helper function to print current statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        try:
            # Extract status code and file size (last two items in the line)
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update file size
            total_size += file_size

            # Update status code count if valid
            if status_code in status_counts:
                status_counts[status_code] += 1

        except (IndexError, ValueError):
            # If line is malformed, skip it
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats before exiting
    print_stats()
    raise

# Print final stats when EOF (Ctrl+D or pipe ends)
print_stats()

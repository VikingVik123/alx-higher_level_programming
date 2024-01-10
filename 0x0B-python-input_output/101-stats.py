#!/usr/bin/python3
"""
Reads from standard input and computes metrics.
"""

import sys
import signal

def compute_metrics(lines):
    total_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    for line in lines:
        # Split the input line
        parts = line.split()

        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update total size
        total_size += file_size

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

    return total_size, status_code_counts

def print_statistics(total_size, status_code_counts):
    # Print total file size
    print(f'Total file size: {total_size}')

    # Print number of lines by status code
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f'{code}: {count}')

def main():
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) % 10 == 0:
                total_size, status_code_counts = compute_metrics(lines)
                print_statistics(total_size, status_code_counts)
                lines = []

    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (CTRL + C)
        total_size, status_code_counts = compute_metrics(lines)
        print_statistics(total_size, status_code_counts)
        sys.exit(0)

if __name__ == "__main__":
    # Register signal handler for SIGINT (CTRL + C)
    signal.signal(signal.SIGINT, signal.SIG_IGN)


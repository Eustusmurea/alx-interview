#!/usr/bin/python3
"""
log parsing
"""

import sys
import re


def output(log_global: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log_global["file_size"]))
    for code in sorted(log_global["code_frequency"]):
        if log_global["code_frequency"][code]:
            print("{}: {}".format(code, log_global["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+] "GET /projects/260 '
        r'HTTP/1.1" (.{3}) (\d+)')

    line_count = 0
    log = {"file_size": 0, "code_frequency": {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # File size
                log["file_size"] += file_size

                # status code
                if code.isdecimal():
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log)
    finally:
        output(log)

import sys

def analyze_log(file_path):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(file_path, "r") as file:
        for line in file:
            for level in counts:
                if line.startswith(level):
                    counts[level] += 1

    return counts


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    result = analyze_log(log_file)

    print("Log Analysis Summary:")
    for level, count in result.items():
        print(f"{level}: {count}")

    # Fail CI if errors exist
    if result["ERROR"] > 0:
        print("ERRORS detected in log file. Failing build.")
        sys.exit(1)

    print("No critical errors found. Build successful.")

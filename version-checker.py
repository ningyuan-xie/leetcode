# This script prints the Python version information.
import sys


def main():
    # Get the Python version information
    version_info = sys.version_info
    # Convert the version information into a string
    version = ".".join(map(str, version_info[:3]))
    print("Python version:", version)


if __name__ == "__main__":
    main()

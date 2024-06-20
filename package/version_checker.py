# This script prints the Python version information.
import sys


def main():
    # Get the Python version information
    version_info = sys.version_info
    # Convert the version information into a string through map function and join method
    # The map function takes a list and applies a function to each member of the list
    # and returns a second list that is the same size as the first
    version = ".".join(map(str, version_info[:3]))
    print("Python version:", version)


if __name__ == "__main__":
    main()

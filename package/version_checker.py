# This script prints the Python version information.
import sys


def main():
    # major, minor, micro, releaselevel, serial
    version_info = sys.version_info
    # version_info[:3] returns a tuple which is an iterable: (major, minor, micro)
    # map takes this tuple and returns a map object which is an iterable
    # ".".join() concatenates the iterable into a string with "." as the separator
    version = ".".join(map(str, version_info[:3]))
    print("Python version:", version)


if __name__ == "__main__":
    main()

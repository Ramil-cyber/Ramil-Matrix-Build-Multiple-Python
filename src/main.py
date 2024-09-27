import os
import sys
import re


def os_and_sys_version():
    python_version = re.search(r"\d+\.\d+", sys.version).group()
    os_name = os.getenv("RUNNER_OS")
    return python_version, os_name


if __name__ == "__main__":
    print(os_and_sys_version())

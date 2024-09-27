from src.main import os_and_sys_version


def test_extended_system():
    python_ver, sys_ver = os_and_sys_version()

    os_list = ["Windows", "Linux", "macOS", "Ubuntu"]
    python_ver_list = ["3.6", "3.7", "3.8", "3.9", "3.10", "3.11"]

    # Check if the Python version is within the expected range
    assert python_ver in python_ver_list, f"Python version {python_ver} not supported."

    # Check if the OS is valid or if it's an unknown but non-empty string
    if sys_ver:
        assert sys_ver in os_list, f"Operating system {sys_ver} not supported."
    else:
        # Ensure sys_ver isn't None or an empty string
        assert sys_ver != "", "Operating system version cannot be an empty string."


if __name__ == "__main__":
    test_extended_system()

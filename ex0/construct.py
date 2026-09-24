#!/usr/bin/env python3
import sys
import os


def construct() -> None:
    if sys.base_prefix == sys.prefix:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        version = f"{sys.version_info.major}.{sys.version_info.minor}"
        site_packages = f"{sys.prefix}/lib/python{version}/site-packages"
        print(site_packages)


if __name__ == "__main__":
    construct()

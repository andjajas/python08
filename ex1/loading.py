#!/usr/bin/env python3
from importlib import import_module


def check_dependencies() -> None:
    DEPENDENCIES: dict[str, str | None] = {}
    mod_list: dict[str, str] = {
        "pandas":"Data manipulation ready",
        "numpy":"Numerical computation ready",
        "matplotlib":"Visualization ready"
        }
    for mod_key in mod_list.keys():
        try:
            mod = import_module(mod_key)
        except ImportError:
            DEPENDENCIES[mod_key] = None
        else:
            DEPENDENCIES[mod_key] = mod.__version__
        if not DEPENDENCIES[mod_key]:
            print(f"[MISSING] {mod_key}")
        else:
            print(
                f"[OK] {mod_key} "
                f"({DEPENDENCIES[mod_key]}) - {mod_list[mod_key]}"
            )


if __name__ == "__main__":
    check_dependencies()

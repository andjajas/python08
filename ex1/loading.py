#!/usr/bin/env python3
from importlib import import_module


def check_dependencies() -> bool:
    dependencies: dict[str, str | None] = {}
    mod_list: dict[str, str] = {
        "pandas":"Data manipulation ready",
        "numpy":"Numerical computation ready",
        "matplotlib":"Visualization ready"
        }
    print("Checking dependencies:")
    for mod_key in mod_list.keys():
        try:
            mod = import_module(mod_key)
        except ImportError:
            dependencies[mod_key] = None
        else:
            dependencies[mod_key] = mod.__version__
        if dependencies[mod_key] is None:
            print(f"[MISSING] {mod_key}")
        else:
            print(
                f"[OK] {mod_key} "
                f"({dependencies[mod_key]}) - {mod_list[mod_key]}"
            )
    return all(dependencies[mod_key] for mod_key in mod_list.keys())


def loading() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    import_dependencies: bool = check_dependencies()


if __name__ == "__main__":
    loading()

#!/usr/bin/env python3
from importlib import import_module


def check_dependencies() -> bool:
    dependencies: dict[str, str | None] = {}
    mod_list: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
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
    dependencies_ok: bool = check_dependencies()
    if not dependencies_ok:
        print("dependencies not found: install using pip or Poetry:")
        print(" for pip:")
        print("     pip install -r requirements.txt")
        print(" for Poetry:")
        print("     poetry install")
        print("Then run this program again.")
    else:
        analyze_matrix()


def analyze_matrix() -> None:
    import numpy as np
    data = np.random.randint(33, 127, size=10)
    print(data)
    import pandas as pd
    df = pd.DataFrame({"codepoint": data})
    print(df)
    df["char"] = df["codepoint"].apply(chr)
    print(df)
    import matplotlib.pyplot as plt
    plt.hist(df["codepoint"], bins=20)
    plt.savefig("matrix_analysis.png")

if __name__ == "__main__":
    loading()

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
        print(" # for pip:")
        print("     pip install -r requirements.txt")
        print(" # then to run the program after pip install:")
        print("     python3 loading.py")
        print(" # for Poetry:")
        print("     poetry install")
        print(" # then to run the program with poetry:")
        print("     poetry run python3 loading.py")
    else:
        analyze_matrix()


def analyze_matrix() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    plt.style.use("dark_background")
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    x = np.random.randint(42, 127, size=1000)
    y = np.random.randint(33, 127, size=1000)
    # create table with 1000 rows and 2 columns (x and y)
    df = pd.DataFrame({"x": x, "y": y})
    # add a third column char
    df["char"] = df["y"].apply(chr)
    sample = df.sample(n=442)
    print("Generating visualization...\n")
    for px, py, ch in zip(sample["x"], sample["y"], sample["char"]):
        plt.text(px, py, ch, color="#00ff41")
    plt.xlim(42, 127)
    plt.ylim(33, 127)
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    loading()

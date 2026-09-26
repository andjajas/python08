#!/usr/bin/env python3
from importlib import import_module


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
    if DEPENDENCIES[mod_key] == None:
        print(f"[MISSING] {mod_key}")
    else:
        print(f"[OK] {mod_list.key()} {DEPENDENCIES[mod_key]} - {mod_list.value()}")

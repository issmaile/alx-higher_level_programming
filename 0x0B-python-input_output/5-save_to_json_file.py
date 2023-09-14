#!/usr/bin/python3
"""asdasd"""
import json


def save_to_json_file(my_obj, filename):
    """asdasd"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

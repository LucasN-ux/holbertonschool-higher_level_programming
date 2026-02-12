#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as f:
        return json.dump(data, f)

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, "r",) as f:
        return json.load(f)

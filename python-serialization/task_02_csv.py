#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as csvfile:
            data = list(csv.DictReader(csvfile))
        with open("data.json", "w") as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False

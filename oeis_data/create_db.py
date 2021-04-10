import csv

import sqlite_utils


def _run(db_name, data_source):
    db = sqlite_utils.Database(db_name)
    with open(data_source) as f: 
        db["sequences"].insert_all(
            csv.DictReader(f)
        )


def run():
    _run("data/sequences.db", "raw/stripped")

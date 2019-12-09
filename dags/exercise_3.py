import airflow
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

import requests

import time
import zipfile
import os

YEAR_RANGES = [(1880, 1899), (1900, 1949), (1950, 1999), (2000, 2018)]


def unzip_names(**kwargs):
    input_file = "/tmp/work/names.zip"
    names_directory = "/tmp/work/"

    print("Starting unzipping...")
    zip_ref = zipfile.ZipFile(input_file, "r")
    zip_ref.extractall(names_directory)
    zip_ref.close()
    print("Unzip finished!")


def find_common(start_year, end_year):
    names_directory = "/tmp/work"

    files = os.listdir(names_directory)
    names = {}

    print("Finding common name...")
    for f in files:
        given_year = int(f[3:7]) if f.endswith(".txt") else None
        if f.endswith(".txt") and start_year < given_year < end_year:
            with open(os.path.join(names_directory, f)) as current:
                for row in current:
                    name, gender, count = row.split(",")
                    if name in names:
                        names[name] += int(count)
                    else:
                        names[name] = int(count)

    common_name = sorted(names, key=names.get, reverse=True)[0]
    print("Common name is {}".format(common_name))

    return common_name


# dag


# tasks

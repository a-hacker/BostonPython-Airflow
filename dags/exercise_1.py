import airflow
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

import requests

import time
import zipfile
import os


def unzip_names(**kwargs):
    input_file = "/tmp/work/names.zip"
    names_directory = "/tmp/work/"

    print("Starting unzipping...")
    zip_ref = zipfile.ZipFile(input_file, "r")
    zip_ref.extractall(names_directory)
    zip_ref.close()
    print("Unzip finished!")


def find_common():
    names_directory = "/tmp/work"

    files = os.listdir(names_directory)
    names = {}

    print("Finding common name...")
    for f in files:
        if f.endswith(".txt"):
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


# dependencies

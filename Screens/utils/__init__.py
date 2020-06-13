import json
import os


def get_data(name):
    filepath = os.path.join('data', '{}.json'.format(name))
    data = json.load(open(filepath))
    return data

import os


def test_load_json_file():
    assert os.path.exists('../operations.json')
    assert os.path.splitext('operations.json')[1] == '.json'



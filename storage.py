# Copyright (C) 2023 twyleg
import json


class Test:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __str__(self):
        return f"name={self.name}, id={self.id}"


def test_add(name: str, id: int) -> None:
    test = Test(name, id)
    test_storage.append(test)


def test_get_by_id(id: int) -> str:
    for test in test_storage:
        if test.id == id:
            return json.dumps(test.__dict__)

    raise Exception("Object not found")


def test_get_by_name(name: str) -> str:
    for test in test_storage:
        if test.name == name:
            return json.dumps(test.__dict__)

    raise Exception("Object not found")



test_storage = []
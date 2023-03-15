import json
from types import SimpleNamespace


class Record:
    def __init__(self, title: str, description: str, uid: int):
        self.title = title
        self.description = description
        self.uid = uid

    @staticmethod
    def from_json(data: str):
        #data = json.loads(json_string, object_hook=lambda d: SimpleNamespace(**d))
        return Record(
            data.fields.Title,
            data.fields.Description,
            data.id
        )

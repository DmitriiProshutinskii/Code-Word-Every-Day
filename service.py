import requests

from data import Record
from random_text import TipOfTheDay, ThirtyTips


class Service:
    def __init__(self):
        f = open(".token", "r")
        self.token = f.read()
        self.base_url = "https://api.airtable.com/v0"

    def get_tips(self, base_id: str, table_id: str) -> ThirtyTips:
        url = self.base_url + f"/{base_id}/{table_id}"
        headers = {"Content-Type": "application/json; charset=utf-8", "Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        records_ = ThirtyTips(response.json())
        return records_

    def get_record(self, base_id: str, table_id: str, record_id: str) -> TipOfTheDay:
        url = self.base_url + f"/{base_id}/{table_id}/{record_id}"
        headers = {"Content-Type": "application/json; charset=utf-8", "Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        record = TipOfTheDay.from_json(response.json())
        return record


if __name__ == '__main__':
    records = Service().get_tips("appCixhrwO39DH3D5", "tbly63ArWXouoPqVR")
    random = records.get_random_text()
    print(random)
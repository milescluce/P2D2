import time
from p2d2 import Database
from pandas import DataFrame

class Company:
    name: str
    location: str
    employees: str
    market_cap: int

class PhazebreakDB(Database):
    company: Company

if __name__ == "__main__":
    d = PhazebreakDB()
    company: DataFrame = d.company
    api = d._api
    api.thread.start()
    time.sleep(100000)
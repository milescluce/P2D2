import time
from p2d2 import Database
from pandas import DataFrame

class Company:
    _unique_keys = ["name", "location"]
    name: str
    location: str
    employees: str
    market_cap: int
    nan_debug: bool

class MyDatabase(Database):
    company: Company

if __name__ == "__main__":
    d = MyDatabase()
    company: DataFrame = d.company
    print(d._unique_keys)
    print(d.read("company", **{"name": "foo"}))
    data = {
        "name": "foo",
        "location": "bar",
        "employees": "99",
        "market_cap": 400
    }
    d.create("company", **data, signature="foobar")
    # api = d._api
    # api.thread.start()
    time.sleep(100000)
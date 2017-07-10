"""database server module

Exposes the `DBStore` wrapper through REST protocol to other services.

`/write` PUT method, used by the Algorithm service to write data into the database.

`/fetch` POST method, given the JSON body of the request
witch contains the constraints as a JSON object, fetches data from database.
"""

# Author: Alexandru Burlacu
# Email:  alexandru-varacuta@bookvoyager.org

import json
import hug
from db_interface import DBStore



with open("config.json") as config_ptr:
    config = json.load(config_ptr)

db_address_port = config["db_addr_port"]
database = DBStore(db_address_port)


api = hug.route.API(__name__)
api.post("/fetch")(database.fetch_with_constraints)
api.put("/write")(database.write_all)

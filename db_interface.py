"""databse interface/wrapper module

Defines a wrapper to be exposed via REST to other services
for a more restricted way to interact with the database.

Also here's defined the `QueryBuilder` class to be implemented,
that will provide a simple DSL to query the `DBStore`.

Sample query:
```

  .find({"age": {"$gt": 18}}, "gender": "F")
  where age > 18 and gender = F

  .find({"name": {"$in": ["Alex", "Jora", "Costea"]}})
  where name in Alex, Jora, Costea


```
"""

# Author: Alexandru Burlacu
# Email:  alexandru-varacuta@bookvoyager.org

from pymongo import MongoClient
import json
from bson import json_util

class DBStore:
    """Convenient wrapper for operations over the database.

    `write_all` method is used, by convention, by the Algorithm service,
    while the `fetch_with_contraints` by the Recommendation service.
    """
    def __init__(self, addr):
        self._client = MongoClient(addr)
        self.coll = self._client.BookVoyagerStore \
                        .get_collection("BookFeatures")

    def write_all(self, source):
        """Given the source iterator,
        dumps all documents (JSON-like) to database."""
        processed = (data for data in source)
        self.coll.insert_many(processed)

    def fetch_with_constraints(self, constraints):
        """Given constraints, a.k.a. the query dict,
        fetches documents (JSON-like) from database."""
        response = self.coll.find(json.loads(constraints))
        return json_util.dumps({"resp": list(response)})

class QueryBuilder:
    """TBI"""
    def __init__(self):
        NotImplemented

    def build(self):
        """Builds the dict query from the given arguments"""
        NotImplemented

# Database Service

Here are all files responsible for The Database, that is:

- `db_interface.py` that defines means to interact with DB through class methods.
- `db_endpoints.py` wraps methods defined in the `db_interface.py` in RESTful API endpoints.
    - __PUT__ */write* dumps a collection of BSONs/JSONs/dicts to the database.
    - __POST__ */fetch* fetches data from database according to provided constraints

## Installation

Initially, you need `python` 3.5.x or higher and `virtualenv` to be installed on your machine, also you need MongoDB v3.4.x.

```bash
    # to keep the namespace clean
    virtualenv -p python3 .venv

    # to install dependencies
    pip install -r requirements.txt

    # enter the virtual environment
    source .venv/bin/activate
```

## Testing

No tests available.

## Profiling

No profiling scripts or suggestions available.

## Style Guide

Full PEP8 [here](https://www.python.org/dev/peps/pep-0008/) compliance. You may use PyLint. 1 tab must be 4 spaces wide. Don't use tab character. Configure your editor accordingly. Docstrings must follow NumPy/SciPy style [here](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt).


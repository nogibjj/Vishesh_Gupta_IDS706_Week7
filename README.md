# Vishesh_Gupta_IDS706_Week5

[![CI](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Vishesh_Gupta_IDS706_Week5/actions/workflows/cicd.yml)

## Project Overview

This project demonstrates how to connect to a SQL database, perform CRUD (Create, Read, Update, Delete) operations, and write SQL queries within a Python script. The project includes:
1. Database connection to an SQLite database.
2. Basic CRUD operations.
3. Two different SQL queries.
4. Implementation of a CI/CD pipeline to automate testing.
5. A simple README file.

```
Vishesh_Gupta_IDS706_Week5/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── data/
│   └── match_results.csv
├── Makefile
├── python_main.py
├── mylib/
│   ├── __pycache__
│   ├── __init__.py
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── test_results.md
├── README.md
├── requirements.txt
├── MatchResultsDB.db
└── main_test.py
```

## Requirements

### 1. **Database Connection**
The Python script connects to an SQLite database using the `sqlite3` module. The database is dynamically created if it doesn't already exist. All database operations are conducted within this connection.

### 2. **CRUD Operations**
We demonstrate the following CRUD operations:
- **Create:** Insert new records into a table.
- **Read:** Query and retrieve records from the table.
- **Update:** Modify existing records within the table.
- **Delete:** Remove records from the table.

## Check format and test errors 
1. Format code `make format`
2. Lint code `make lint`
3. Test code `make test`
Additionally we have create a few more make commands that are:
4. extract: run `make extract`
5. transform and load: run `make transform_load`

## References 
https://github.com/nogibjj/sqlite-lab
https://learn.microsoft.com/en-us/azure/databricks/dev-tools/python-sql-connector


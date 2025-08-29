# Order Management CLI App

## What it is
A simple Python command-line app to manage orders and products using a database.

## Files
- lib/db/models.py – Defines database tables and data models
- lib/db/seed.py – Adds sample data to the database
- lib/cli.py – The command-line interface for users
- lib/helpers.py – Helper functions for the CLI
- lib/debug.py – Tools for debugging
- Pipfile – Project dependencies

## How to use
1. Install packages with `pipenv install`
2. Add test data with `python lib/db/seed.py`
3. Run the app: `python lib/cli.py`

## What you can do
- Manage orders and products: add, list, delete, find
- See products linked to each order
- Enjoy clear messages and input checks

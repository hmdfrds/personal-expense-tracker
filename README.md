# Personal Expense Tracker (CLI)

## Overview

A simple command-line expense tracker that lets users log, edit, delete and analyze expenses.

## Features

- Add, list, edit, delete expenses
- Filter expenses by date range and category
- Generate reports
- Import/export data in JSON format
- Fully tested with pytest
- Beautiful CLI using Click & Rich

## Instalation

Clone the repository:

```bash
git clone https://github.com/hmdfrds/personal-expense-tracker
cd personal-expense-tracker
pip install -r requirements.txt
```

## Usage

Run the CLI:

```bash
python src/main.py
```

## Available Commands:

```bash
python src/main.py add
python src/main.py list
python src/main.py edit --id <expense_id>
python src/main.py delete --id <expense_id>
python src/main.py search-date --start DD-MM-YYYY --end DD-MM-YYYY
python src/main.py search-category --category <category>
python src/main.py report
python src/main.py export --file <export_file_path>
python src/main.py import-expenses --file <import_file_path>
```

## TEsting

Run tests:

```bash
pytest
```

## License

MIT License

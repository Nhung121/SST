Setup instructions

- create requirements.txt
- Create virtual environment: `python3 -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Install: 
`python -m ipykernel install --user --name=.test`

How to convert netcdf file to csv:
- Create virtual environment: `python3 -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Run script: `python convert-netcdf-to-csv.py`
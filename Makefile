FLASK_APP = src/app.py
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run: $(VENV)/bin/activate
	$(PYTHON) -m flask run

test:
	$(PYTHON) -m pytest

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf src/__pycache__
	rm -rf venv


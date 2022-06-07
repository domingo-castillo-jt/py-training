FLASK_APP = src/index.py
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run: $(VENV)/bin/activate
	$(PYTHON) -m flask run

get_items: $(VENV)/bin/activate
	$(PYTHON) src/core/use_cases/get_all_items_use_case.py

test:
	$(PYTHON) -m pytest

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf src/__pycache__
	rm -rf venv

lint:
	mypy src/*.py && \
	black src/ && \
	flake8 src/ && \
	isort src/ 

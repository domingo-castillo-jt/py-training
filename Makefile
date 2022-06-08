FLASK_APP = src/index.py
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run: $(VENV)/bin/activate
	$(PYTHON) -m flask run
	
## Start the service manually when in debug mode.
debug:
	export FLASK_ENV=development &&\
	export FLASK_SETTINGS_MODULE=development &&\
	flask run --host=0.0.0.0 --port=8080 --without-threads

get_items: $(VENV)/bin/activate
	$(PYTHON) -m flask cli get-all-items

test:
	$(PYTHON) -m pytest

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf src/__pycache__
	rm -rf venv

lint:
	isort src/ && \
	black src/ && \
	flake8 src/ && \
	mypy src/*.py

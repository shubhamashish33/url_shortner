### help - help docs for this Makefile
.PHONY: help
help :
	@sed -n '/^###/p' Makefile

### install - install requirements in venv
.PHONY: install
install:
	python3 -m venv .env; \
	. .env/bin/activate; \
	pip install -r requirements.txt

### start - start flask dev server
.PHONY: start
start:
	. .env/bin/activate; \
	python app.py

### lint - lint code
.PHONY: lint
lint:
	isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=100 .
	black --line-length=100 .
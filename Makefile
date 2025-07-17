SRC=app
TESTS=tests

test:
	pytest --cov=$(SRC) $(TESTS) --cov-report=term --cov-report=html

coverage:
	xdg-open htmlcov/index.html || open htmlcov/index.html

check-format:
	black --check $(SRC) $(TESTS)

format:
	black $(SRC) $(TESTS)

install:
	pip install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache htmlcov .mypy_cache .coverage
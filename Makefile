install:
	poetry install

test:
	poetry run pytest tests -vv

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml tests/

lint:
	poetry run flake8 page_loader

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

.PHONY: install test test-coverage lint selfcheck check build publish package-install

.PHONY: install virtualenv ipython


install:
		@echo "Installing for dev environment"
		@.\.venv\Scripts\python -m pip install -e '.[test]'

virtualenv:
		@.\.venv\Scripts\python -m pip -m venv .venv


ipython:
		@.\.venv\Scripts\ipython

test:
		@.\.venv\Scripts\pytest.exe

watch:
		@.\.venv\Scripts\ptw.exe

clean:            ## Clean unused files.
		@find ./ -name '*.pyc' -exec rm -f {} \;
		@find ./ -name '__pycache__' -exec rm -rf {} \;
		@find ./ -name 'Thumbs.db' -exec rm -f {} \;
		@find ./ -name '*~' -exec rm -f {} \;
		@rm -rf .cache
		@rm -rf .pytest_cache
		@rm -rf .mypy_cache
		@rm -rf build
		@rm -rf dist
		@rm -rf *.egg-info
		@rm -rf htmlcov
		@rm -rf .tox/
		@rm -rf docs/_build
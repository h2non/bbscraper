all: check_dependencies test

export PYTHONPATH:= ${PWD}
export BBSCRAPER_DEPENDENCIES:= beautifulsoup4

check_dependencies:
	@echo "Checking for dependencies to run tests ..."
	@for dependency in `echo $$BBSCRAPER_DEPENDENCIES`; do \
		python -c "import $$dependency" 2>/dev/null || (echo "You must install $$dependency in order to run bbscraper's tests" && exit 3) ; \
		done

test:
	@echo "Running unit tests ..."
	@python -m unittest discover

publish:
	@python setup.py sdist register upload
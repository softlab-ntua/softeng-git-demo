.PHONY: default setup venv deps clean distclean tests

VIRTUALENV=virtualenv
VIRTUALENV_OPTS=--no-site-packages
VIRTUALENV_DIR=venv

default: tests

setup: venv

venv:
	test -d $(VIRTUALENV_DIR) \
	  || ($(VIRTUALENV) $(VIRTUALENV_OPTS) $(VIRTUALENV_DIR) || true)
	@echo "Don't forget to: source $(VIRTUALENV_DIR)/bin/activate"
	@echo "Then, make deps"

deps:
	pip install -Ur requirements.txt

clean:
	$(RM) *~

distclean: clean
	$(RM) -fr venv/

tests:
	python -m unittest discover

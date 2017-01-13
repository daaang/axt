PY=python3
SETUP=$(PY) setup.py
GENERATED_DIRS=lib/Axt.egg-info build dist
QUICKTEST=unittests/.quick_test.sh
FULLTEST=unittests/.test_and_clean.sh

build: setup.py
	$(SETUP) build

dist: build
	$(SETUP) sdist
	$(SETUP) bdist_wheel

install: build
	$(SETUP) install

clean:
	touch $(GENERATED_DIRS) del.c __pycache__
	rm -r $(GENERATED_DIRS)
	find . -name '*.c' | xargs rm
	find . -name __pycache__ | xargs rm -r

test: clean build
	bash $(FULLTEST)

quicktest: build
	bash $(QUICKTEST)

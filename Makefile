PY=python3

build: setup.py
	$(PY) setup.py build

dist: build
	$(PY) setup.py sdist
	$(PY) setup.py bdist_wheel

install: build
	$(PY) setup.py install

clean:
	touch lib/Axt.egg-info build dist del.c __pycache__
	rm -r lib/Axt.egg-info build dist
	find . -name '*.c' | xargs rm
	find . -name __pycache__ | xargs rm -r

test: clean build
	bash run_tests.sh

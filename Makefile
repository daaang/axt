PY=python3

build: setup.py
	$(PY) setup.py build

dist: build
	$(PY) setup.py sdist
	$(PY) setup.py bdist_wheel

test: build
	PYTHONPATH=build/lib.linux-x86_64-3.4 $(PY) -m unittest

clean:
	touch lib/Axt.egg-info build dist
	rm -r lib/Axt.egg-info build dist

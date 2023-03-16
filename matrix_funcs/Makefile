PYTHON_PATH := ../venv/bin/python

.PHONY: clear build

clear:
	rm -rf ./build
	rm -rf ./matrix_funcs.egg-info
	rm -rf ./dist


build:
	$(PYTHON_PATH) setup.py install

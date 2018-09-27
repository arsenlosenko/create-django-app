.PHONY: venv
.PHONY: upload
.PHONY: deps
.PHONY: clean

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*
		
deps:
	pip install -r requirements.txt
	
clean:
	rm -rf build dist *.egg-info
	
venv:
	source venv/bin/activate


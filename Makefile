clean:
	rm -rf venv

build_env:
	rm -rf venv
	python3 -m venv venv
	./venv/bin/python3 -m pip install --upgrade pip
	./venv/bin/pip3 install -r requirments.txt

run:
	./venv/bin/python3 App.py
SRC = $(wildcard $(DB_DIR)/*.csv.7z)

DB_DIR = DataSet
DB = $(SRC:.csv.7z=.csv)

clean:
	rm -rf venv

build_env:
	rm -rf venv
	python3 -m venv venv
	./venv/bin/python3 -m pip install --upgrade pip
	./venv/bin/pip3 install -r requirments.txt

run: extract
	./venv/bin/python3 App.py

%.csv : %.csv.7z
	7z x $< -o$(DB_DIR) -y

extract: $(DB)

clean_extract:
	rm -f $(DB)
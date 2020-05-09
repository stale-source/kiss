venv:
	virtualenv venv
	venv/bin/pip install -r requirements.txt

test: venv
	pytest .
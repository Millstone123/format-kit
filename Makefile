bootstrap:
	pip install -r requirements.txt -q 2>&1 | tail -1
	python3 -m pytest tests -q

test:
	python3 -m pytest tests -q

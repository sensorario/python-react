.PHONY: fmt lint typecheck test

fmt:
	black .
	ruff check . --fix

lint:
	ruff check .

typecheck:
	mypy .

test:
	PYTHONPATH=. pytest ../backend

server:
	uvicorn main:app --reload

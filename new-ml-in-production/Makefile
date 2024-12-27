.PHONY: run_builder run_inference runner_builder runner_inference install check run clean
.DEFAULT_GOAL:=runner_inference

runner_builder: check run_builder clean

runner_inference: check run_inference clean

run_builder: install
	cd new_ml_in_production; poetry run python3 runner_builder.py

run_inference: install
	cd new_ml_in_production; poetry run python3 runner_inference.py

install: pyproject.toml
	poetry install

check:
	poetry run ruff check

clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf .ruff_cache




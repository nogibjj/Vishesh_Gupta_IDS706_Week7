install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	ruff check *.py

format:	
	black *.py 

test:
	python -m pytest -cov=main main_test.py
		
all: install lint format test

generate_and_push:
	# Create the markdown file 
	python main_test.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log as test_results.md"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi
cd test
coverage run -m unittest && cd .. && flake8 --exclude build --max-line-length 89 --ignore=F401
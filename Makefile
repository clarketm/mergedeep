project:=mergedeep
version:=$(shell python -c 'import sys, os; sys.path.insert(0, os.path.abspath(".")); print(__import__("${project}").__version__)')

.PHONY: list
list help:
	@make -pq | awk -F':' '/^[a-zA-Z0-9][^$$#\/\t=]*:([^=]|$$)/ {split($$1,A,/ /);for(i in A)print A[i]}' | sed '/Makefile/d' | sort

.PHONY: format
format:
	python -m black .

.PHONY: build
build: clean
	rm -rf ./dist/*
	python3 setup.py sdist bdist_wheel

.PHONY: test
test:
	pyenv local 3.5.6 3.6.8 system
	python -m tox

.PHONY: clean
clean:
	rm -rf ./dist ./build ./*.egg-info ./htmlcov
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: check
check:
	twine check dist/*

.PHONY: upload-test
upload-test: test clean build check
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: tag
tag:
ifeq (,$(shell git tag --list | grep "${version}"))
	git tag "v${version}"
endif

.PHONY: release
release: tag
ifdef version
	curl -XPOST \
	-H "Authorization: token ${GITHUB_ACCESS_TOKEN}" \
	-H "Content-Type: application/json" \
	"https://api.github.com/repos/clarketm/${project}/releases" \
	--data "{\"tag_name\": \"v${version}\",\"target_commitish\": \"master\",\"name\": \"v${version}\",\"draft\": false,\"prerelease\": false}"
endif

.PHONY: upload
publish upload: test clean build check
	twine upload dist/*


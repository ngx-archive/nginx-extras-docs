.PHONY: all
all:clean
	virtualenv-3 ./venv
	./venv/bin/pip install -r requirements.txt
	./venv/bin/python ./generate.py
	./generate.sh

.PHONY: clean
clean:
	find resty ! -name 'core.yml' -type f -exec rm -f {} +
	rm -rf *.spec

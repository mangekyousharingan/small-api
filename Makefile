run:
	cd ./src && python main.py

run-dokcer:
	docker-compose build && docker-compose up

test:
	cd ./src && PYTHONPATH=. pytest ../tests

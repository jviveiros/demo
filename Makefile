build:
	docker-compose build
	@echo "All built 🏛"

up:
	docker-compose up
	@make logs

.PHONY: logs
logs:
	docker-compose logs -f

down:
	docker-compose stop


clean:
	@echo "Deleting exited containers..."
	docker ps -a -q -f status=exited | xargs docker rm -v
	@echo "Deleting dangling images..."
	docker images -q -f dangling=true | xargs docker rmi
	@echo "Clean"

restart:
	@echo "make down => make up"
	@make down
	@make up


rebuild:
	@echo "make down => make build => make up"
	@make down
	@make build
	@make up




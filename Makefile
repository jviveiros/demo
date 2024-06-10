build:
	podman-compose build
	@echo "All built 🏛"

up:
	podman-compose up
	@make logs

.PHONY: logs
logs:
	podman-compose logs -f

down:
	podman-compose stop


clean:
	@echo "Deleting exited containers..."
	podman ps -a -q -f status=exited | xargs podman rm -v
	@echo "Deleting dangling images..."
	podman images -q -f dangling=true | xargs podman rmi
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




NAME=slavpetroff/sweetshop
VERSION=`git describe --always`
BRANCH=$(shell echo $(CI_BUILD_REF_NAME))
CONTAINER_IP=$(shell echo $(docker-machine ip default))
CURRENT_LOCATION := ${CURDIR}
CURRENT_LOCATION~= $(CURRENT_LOCATION):"/django"
IMAGE_NAME='django'

ifeq ($(shell echo $(BRANCH)),master || $(shell echo $(BRANCH)),HEAD)
	TAG='master'
else
	ifeq ($(BRANCH),)
		TAG='master'
	else
		TAG=$(BRANCH)
	endif
endif

NO_COLOR=\033[0m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m

OK_STRING=$(OK_COLOR)[OK]$(NO_COLOR)
IP_STRING=$(OK_COLOR)$$(docker-machine ip default):80$(NO_COLOR)
ERROR_STRING=$(ERROR_COLOR)[ERRORS]$(NO_COLOR)
WARN_STRING=$(WARN_COLOR)[WARNINGS]$(NO_COLOR)

AWK_CMD = awk '{ printf "%-30s %-10s\n",$$1, $$2; }'
PRINT_ERROR = printf "$@ $(ERROR_STRING)\n" | $(AWK_CMD) && printf "$(CMD)\n$$LOG\n" && false
PRINT_WARNING = printf "$@ $(WARN_STRING)\n" | $(AWK_CMD) && printf "$(CMD)\n$$LOG\n"
PRINT_OK = printf "$@ $(OK_STRING)\n" | $(AWK_CMD)
PRINT_IP = printf "$@ $(IP_STRING)\n" | $(AWK_CMD)
BUILD_CMD = LOG=$$($(CMD) 2>&1) ; if [ $$? -eq 1 ]; then $(PRINT_ERROR); elif [ "$$LOG" != "" ] ; then $(PRINT_WARNING); else $(PRINT_OK); fi;


help:
	@echo "*******************************************************"
	@echo "Please use \`make <action>' where <action> is one of:"
	@echo "*******************************************************"
	@echo " container                 to build and start a local container."
	@echo " app                       to prepare and build image."
	@echo " pull                      to pull from Docker Hub."
	@echo " run                       to run a container and mount the django"
	@echo " prepare                   to create local git archive."
	@echo " move_requirements         to move Django`s requirements to Docker."
	@echo " clean                     to remove git archive."
	@echo " clean_docker              to remove containers."
	@echo " push                      to push to Docker Hub."
	@echo " ip                        to display IP:PORT of default container."
	@echo " delete_images             to deletes all images."
	@echo "*******************************************************"

# Pulls a build of the app and starts a local container.
container: pull run ip
	@$(PRINT_OK)

# Build and pushes the app to Docker Hub.
app: move_requirements build clean push
	@$(PRINT_OK)

pull:
	docker pull $(NAME):$(TAG)
	@$(PRINT_OK)

run:
	docker run --name $(IMAGE_NAME) -v $(CURRENT_LOCATION):/var/projects/backend/ --env-file docker/env.conf -p 80:8080 -d $(NAME):$(TAG)
	@$(CURRENT_LOCATION)

prepare:
	git archive -o docker/backend.tar HEAD
	@$(PRINT_OK)

move_requirements:
	cp django/requirements.txt docker/requirements.txt
	@$(PRINT_OK)

build:
	docker build -t $(NAME):$(TAG) --rm docker
	@$(PRINT_OK)

clean:
	rm -f docker/requirements.txt

clean_docker:
	docker rm -f $$(docker ps -a -q)
	@$(PRINT_OK)

push:
	docker push $(NAME):$(TAG)

.PHONY: ip
ip:
	 @$(PRINT_IP)

delete_images:
	docker rmi -f $$(docker images -q)
	@$(PRINT_OK)

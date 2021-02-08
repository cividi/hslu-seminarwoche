.PHONY: all

all: up

up:
	poetry update
	poetry shell
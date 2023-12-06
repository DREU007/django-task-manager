### Hexlet tests and linter status:
[![Actions Status](https://github.com/DREU007/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DREU007/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/242cfd0f231f818c6852/maintainability)](https://codeclimate.com/github/DREU007/python-project-52/maintainability)

### Showcase
[![Showcase example](/showcase/example.gif)]

[TaskManager](https://taskmanager-rd5g.onrender.com/) is a web tool to handle tasks within registered users.

**Features:**
    * Authorisation system
    * CRUD implementation for API (REST like) 
    * Filters for tasks (django-filter)
    * Front-end via Bootstrap (django-bootstrap)
    * Multiple language support: English, Russian 

### Requirements
* Python 3.10
* Poetry
* PostgreSQL (or SQLite)
* Make

### Installation
```
git clone https://github.com/DREU007/django-task-manager
cd django-task-manager
make install
make setup 
cp .env_example .env
```
Fill up .env variables or use the default one.

### Start
To start in development:
`make dev`

To start in production:
`make prod`

### Other commands are available in Makefile

# Backend Anzen Tech Screen
### Roberto de Jesús García

## API Docs
`http://0.0.0.0:8000/docs` or
`http://127.0.0.1:8000/docs`

## Getting Started

* `make up`: to bring up a local docker network running the application and services.
* `make down`: cleanup all the containers.
* `make test`: With the containers running we can also run project unit tests with coverage report.
* `make logs`: show all containers logs.


## DB migrations

`dbmate` makes easy for us to run database migrations regardless of what our backend looks like. After installing dbmate, we’ll make our first migration:
* `dbmate new <migration_name>`

[dbmate install](https://github.com/amacneil/dbmate#installation)

This will create a new file with a name that looks like: `20230101004439_<migration_name>.sql`
# Backend Anzen Tech Screen - Roberto de Jesús García

## Endpoint specifications
### Create insurance application
URI: `api/v1/applications`

Method: `POST`

Body: 

Field Name |   Type   | Description
---|:--------:|---
account_name | `string` | **REQUIRED**. Name of the company (named insured)
lines_coverage |  `list`  | **REQUIRED**. Coverage requested
uw_name | `string` | **REQUIRED**. Underwriting Name
premium | `float`  | **REQUIRED**. Insurance price
state | `string` | Company based state (Defult DC)
effective_date |  `date`  | **REQUIRED**. Insurance start date
expiration_date |  `date`  | **REQUIRED**. Insurance expiration date
sic | `string` | **REQUIRED**. SIC
status | `string` | Application status (Default new)
deal_stage | `string` | Deal status (Default new)

Example

      ```
      {
          "account_name": "ABC Insurance Company",
          "lines_coverage": ["EPLI", "D&O"],
          "uw_name": "Floyd Miles",
          "premium": 12000,
          "state": "DC",
          "effective_date": "2023-01-01",
          "expiration_date": "2023-12-31",
          "sic": "01011 Iron Ores",
          "status": "new",
          "deal_stage": "new"
      }
      ```
Results:
* 200 Ok
  ```
    {
        "application_id": 1
    }
  ```
* 400 Bad request
  ```
    {
        "message": "Invalid data",
        "fields": []
    }
  ```

### Insurance application detail
URI: `api/v1/applications/{application_id}}`

Method: `GET`

Results:
* 200 Ok
  ```
    {
        "application_id": 1,
        "account_name": "ABC Insurance Company",
        "lines_coverage": ["EPLI", "D&O"],
        "uw_name": "Floyd Miles",
        "premium": 12000,
        "state": "DC",
        "effective_date": "2023-01-01",
        "expiration_date": "2023-12-31",
        "sic": "01011 Iron Ores",
        "status": "new",
        "deal_stage": "new"
    }
  ```
* 404 Not found
  ```
    {
        "message": "Application not found"
    }
  ```

### Insurance application list
URI: `api/v1/applications?skip={skip}&limit={limit}`
Optional Params (filters):
  * account_name
  * status
  * lines_coverage
  * uw_name
  * deal_stage
Method: `GET`

Results:
* 200 Ok
  ```
    {
        "items": [
            {
                "application_id": 1,
                "account_name": "ABC Insurance Company",
                "lines_coverage": ["EPLI", "D&O"],
                "uw_name": "Floyd Miles",
                "premium": 12000,
                "state": "DC",
                "effective_date": "2023-01-01",
                "expiration_date": "2023-12-31",
                "sic": "01011 Iron Ores",
                "status": "new",
                "deal_stage": "new"
            }
        ]
    }
  ```

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
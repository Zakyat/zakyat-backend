# Zakyat backend

The backend consists of a [Django](https://docs.djangoproject.com/en/2.2/) project with GraphQL for the API. The database used is MongoDB with the [Djongo](https://nesdis.github.io/djongo/) connector for minimal ORM changes.


## Configration

Create a ".env" file in the root directory with the following contents:
```bash
DB_HOST=db
DB_USERNAME= # Same username set in the mongo container
DB_PASSWORD= # And same password
```
After building the image and running the container, make sure to `docker exec` into the container to create a superuser.

## Running

Running `docker-compose up` in the parent directory should automatically build the image and run the container.

## Useful links

[Entity Relationship Diagram](https://dbdiagram.io/d/5e3536af9e76504e0ef0e7d2)

[Sberbank acquring (payment) system](https://developer.sberbank.ru/doc/v1/acquiring/rest-requests-about)
[Code example for connecting acquring](https://github.com/madprogrammer/django-sberbank)

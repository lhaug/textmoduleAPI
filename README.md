# 🧩 Textmodule API (Python 3 + PostgreSQL + Docker)

Eine containerisierte RESTful API für die Verwaltung von Textmodulen mit FastAPI, PostgreSQL und Docker. 
Jedes Textmodul besteht aus einem eindeutigen `title` und einem frei definierbaren `content` und Metadaten wie dem `creation_date` und dem `last_changed_date`.

---
## ✨ Features

- CRUD-API für Textmodule
- OpenAPI-Dokumentation (`/docs`)

## 🚀 Getting started
Open Docker on your machine.
Then start the container with: 

``` docker-compose up --build ```

⚡ call [localhost:8000/docs#/](http://localhost:8000/docs#/) and use interactive OpenAPI

## 🛑 Shut Down

Shutting down the container, this also deletes the database and all entrys with:

``` docker-compose down -v ```





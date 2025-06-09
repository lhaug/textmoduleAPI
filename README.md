# 🧩 Textmodule API (Python 3 + PostgreSQL + Docker)

This is a containerised RESTful API for managing text modules, built using FastAPI, PostgreSQL and Docker.
A simple GUI is available using Electron.
Each text module consists of a unique title and freely definable content, as well as automatically created metadata such as an identification number, creation date and last modification date.

The API was intentionally kept simple to make it universally applicable. If user management exists, the creator could be attached to each text module. Depending on the context, the component can be extended as required with additional features such as categories, versions or languages.

---
## ✨ Features

- CRUD-API für Textmodule
- OpenAPI-Dokumentation (`/docs`)

## 🚀 Getting started
Open Docker on your machine.
Then start the container with: 

```docker-compose up --build```

### ⚡ using the interactive SwaggerUI 
call [localhost:8000/docs#/](http://localhost:8000/docs#/)

or 

### 🖥️ using a simple GUI
```cd FE/electron```

```npm install```

```npm start```

## 🛑 Shut Down

Shutting down the container, this also deletes the database and all entrys with:

```docker-compose down -v```





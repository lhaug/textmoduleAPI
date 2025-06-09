# 🧩 Textmodule API (Python 3 + PostgreSQL + Docker)

This is a containerised RESTful API for managing text modules, built using FastAPI, PostgreSQL and Docker.
A simple GUI is available using Electron.
Each text module has a unique title and freely definable content. Neither can be empty. Automatically created metadata is also included, such as an identification number, creation date and last modification date.

The API was intentionally kept simple to make it universally applicable. If user management exists, the creator could be attached to each text module. Depending on the context, the component can be extended as required with additional features such as categories, versions or languages.

---
## ✨ Features

- CRUD-API for text modules
- OpenAPI-Documentation (Swagger)
- Simple electron GUI

## 🚀 Getting started

### 1. Start the container

Clone this project.

Open Docker on your machine.

Then start the container with the following command in the project folder: 

```docker-compose up --build```

### ⚡ 2.1 using the interactive SwaggerUI

call [localhost:8000/docs#/](http://localhost:8000/docs#/)

<img width="1440" alt="OpenAPI" src="https://github.com/user-attachments/assets/3a63e895-6484-4db6-b70d-53ae9a41aeb5" />

or 

### 🖥️ 2.2 using the simple GUI

run the following commands in the project folder:

```cd FE/electron```

```npm install```

```npm start```

<img width="802" alt="textmoduleManager" src="https://github.com/user-attachments/assets/daf9094f-d39a-4290-b69b-64f71f8c1e49" />

## 🛑 Shut Down

Shutting down the container, this also deletes the database and all entrys with the following command:

```docker-compose down -v```

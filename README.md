# Project Setup Guide

This repository contains a **Dockerized backend application** with database services.  
Follow the steps below to get your environment up and running.

---

## 1. ⚒️ Requirements/Tools

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Postman](https://www.postman.com/downloads/) (optional)

---

## 2. ⚙️ Environment Variables

- Copy the provided example file:

  ```sh
  cp .env.example .env
  ```

- Adjust values in .env if necessary (e.g. ports, DB name).

- ⚠️ Never commit your .env file. Only .env.example is versioned.

## 3. ⚡Running the Project

Build and start all services:

```sh
docker compose up --build
```

Stop services without removing data:

```sh
docker compose down
```

Stop services and clean volumes (removes DB data):

```sh
docker compose down -v
```

## 4. 🐳 Docker Notes

Docker ps should not list stray processes. After running docker compose down, the project should not leave containers running in the background.

To check:

```sh
docker ps
```

If no containers appear, the environment is clean.

## 5. 🚀 Using Postman

We provide a Postman collection JSON file for easier testing.

1. Open Postman

2. Click Import → Upload Files

3. Select the provided .postman_collection.json from this project

4. The collection will appear in your workspace with predefined requests

- Make sure your .env and Docker services are running before testing.
- Update environment variables in Postman if your host/port differ from defaults.

## 6. 🧩 Code Style

- Prefer explicit naming over abbreviations (e.g. Configuration over Config, but use single-letter inside loops, comprehensions, or context managers)

- Avoid redundant comments — no syntax or “section divider” comments

- Docker Compose manages all components: backend, frontend, PostgreSQL, etc.

- The project loosely follows MVC principles, adapted for Flask’s flexibility:

| Layer          | Folder          | Responsibility                                           |
| -------------- | --------------- | -------------------------------------------------------- |
| **Controller** | `controllers/`  | Defines endpoints and HTTP request/response logic        |
| **Model**      | `models/`       | Defines data contracts and validation using **Pydantic** |
| **Service**    | `services/`     | Business logic, orchestration between repositories       |
| **Repository** | `repositories/` | Database access via raw SQL                              |
| **Utils**      | `utils/`        | Cross-cutting helpers (logging, error handling, etc.)    |

### 🧭 API Naming Convention (Temporary)
- **Current:**  
  - `GET /api/tasks` → Retrieve list of tasks  
  - `POST /api/task` → Create a single task  
  - `PATCH /api/task/:id` → Update a task  
  - `DELETE /api/task/:id` → Delete a task  

- **Rationale:**  
  The singular `/task` for creation emphasizes that a single task is created per request.  
  The plural `/tasks` for listing aligns with REST expectations for collection retrieval.  
  This may be unified to fully plural (`/tasks`) in a future revision once the API stabilizes.
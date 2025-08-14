# Math-microservice

📘 Math Microservice API

A FastAPI-based microservice for authenticated users to perform mathematical operations: power, factorial, and Fibonacci — with modern features like JWT authentication, RabbitMQ logging, Redis caching, and Prometheus/Grafana monitoring.

🚀 How to Run the Application

step 1)Clone the repository
git clone <repo-url>
cd proiect

step 2)Start everything with Docker Compose
docker-compose up --build

step3)Access services:
API docs: http://localhost:8000/docs

RabbitMQ UI: http://localhost:15672 (guest/guest)

Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (admin/admin), you already have a pre-configured dashboard for FastAPI located at: proiect/monitoring/fastapi_grafana_dashboard. This dashboard displays:Total HTTP requests,Request counts per endpoint,Average request duration, Response status code distribution (pie chart)
✅ Functionality Summary

🔐 Authentication & Authorization:

User registration and login

JWT token-based authentication

Role-based access (admin, user)


🧮 Math Endpoints:
/math/pow – power function

/math/factorial – factorial function

/math/fibonacci – computes the nth Fibonacci number


⚡ Fibonacci Optimized:

Implemented using Matrix Exponentiation

Time Complexity: O(log n) with exponentiation by squaring

Auxiliary Space: O(log n) due to recursion stack


💾 Data Persistence:

All requests are saved in operation_requests table

Each request is associated with the user_id of the authenticated user


💬 Asynchronous Logging:

All requests are sent to RabbitMQ (math_queue)

A background worker consumes messages and saves to SQLite DB


🔁 Caching with Redis:

Results are cached per operation (power, factorial, Fibonacci)

Cache keys are based on input parameters (e.g. fibonacci:100)

Time-to-live for each cached value is configurable (default 1h)


📊 Monitoring & Observability:

Prometheus collects metrics from /metrics

Grafana displays dashboards (requests count, duration, status codes)


🐳 Full Containerization:

FastAPI app, worker, Redis, RabbitMQ, Prometheus, Grafana are all Dockerized


🧠 Technologies & Structure

Backend: FastAPI (async), SQLAlchemy (ORM), Pydantic (validation)

Database: SQLite

Cache: Redis

Queue: RabbitMQ + aio-pika

Monitoring: Prometheus + Grafana

Auth: JWT (python-jose)

Container: Docker + Compose


📁 Project Structure
/app
  /controllers    # API routers (math, auth)
  
  /services       # Business logic (math, db)
  
  /models         # ORM models (User, OperationRequest)
  
  /schemas        # Pydantic schemas
  
  /utils          # Caching, messaging, security
  
  /db             # Database engine/session setup
  
  main.py         # FastAPI app entry point
  

/worker/worker.py # Async worker consuming from RabbitMQ

/monitoring/      # Prometheus config & Grafana dashboard


📋 Based on Project Requirements:

This project fulfills all required and "nice to have" criteria from the homework brief:

✅ Mathematical operations exposed via API (not SOAP)

✅ Containerized using Docker Compose

✅ JWT authentication & user tracking

✅ Request persistence via SQLAlchemy + SQLite

✅ Bonus: logging via RabbitMQ queue (math_queue)

✅ Bonus: Redis caching and monitoring with Prometheus/Grafana

✅ MVCS architecture, extensible design





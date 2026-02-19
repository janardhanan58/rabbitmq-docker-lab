# RabbitMQ Docker Lab
This project demonstrates a decoupled messaging system using **Python** and **RabbitMQ** orchestrated with **Docker Compose**.

## Features
- **Persistence**: Uses Docker Volumes to ensure messages survive container restarts.
- **Decoupling**: Separate Producer and Consumer logic.
- **Infrastructure as Code**: Entire environment managed via `docker-compose.yml`.

## How to Run
1. `docker compose up -d`
2. Run Receiver: `docker exec -it python-app python receive.py`
3. Run Sender: `docker exec -it python-app python hello.py`

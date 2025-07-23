# API Status Checker

Simple Python script that checks the HTTP status of URLs listed in `urls.txt` and saves the results to `raport.csv`.

## Features
- HTTP status check
- CSV output
- Docker support
- CI/CD pipeline ready (Azure DevOps)

## How to run locally
```bash
pip install -r requirements.txt
python main.py
```

## How to run in Docker
```bash
docker build -t api-status-checker .
docker run api-status-checker
```

## Sample output
```
https://google.com -> 200
https://github.com -> 200
```

## CI/CD (Azure Pipelines)
This repo contains `azure-pipelines.yml` file that:
- installs dependencies
- runs the script
- publishes `raport.csv` as an artifact

## Author
Created for DevOps Trainee showcase.

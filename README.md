# Job Posting API

## Description

This repository contains the code for a **Job Posting API**, designed to manage job postings and applicants.

- **job_manager**: Model for managing the state of job postings and applicants.
- **models**: Pydantic models for data validation.
- **main**: API endpoints.

## 🛠 Prerequisites

Ensure the following tools are installed on your local machine:


- [Git](https://git-scm.com/) – For pulling the code from GitHub.

Running it via Python:
- [Python 3.8+](https://www.python.org/downloads/) – Required for running the application locally.
- [pip](https://pip.pypa.io/en/stable/) – Python's package installer.

Running it via Docker:
- [Docker](https://www.docker.com/products/docker-desktop) – For building and running the Docker container.

## 🏗 Setup Instructions

### 1️. Clone the Repository

Clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/aaronbau1/job-posting-api.git
cd job-posting-api
```

## Setup Option 1: Running app locally via Python

### 1. Install Dependencies Using pip
```bash
pip install -r requirements.txt
```

### 2. Run the application locally
```bash
uvicorn main:app --reload
```

## Setup Option 2: Building and Running a Docker Image locally

### 1. Build the Docker Image
```bash
docker build -t job-posting-api .
```

### 2. Run the Docker Image
```bash
docker run -d -p 8000:8000 job-posting-api
```

### 3. Access the Application
The api will be available at http://localhost:8000 on your machine. 

### 4. Documentation for API endpoints
API documentation can be found at http://localhost:8000/docs
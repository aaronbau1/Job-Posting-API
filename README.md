# Job Posting API

## Description

This repository contains the code fora ** Job Posting API**, an API designed to manage job postings and applicants.

- **job_manager**: Model for managing the state of job postings and applicants.
- **models**: Pydantic models for data validation.
- **main**: Contains the API endpoints.

## 🛠 Prerequisites

Ensure the following tools are installed on your local machine:

- [Docker](https://www.docker.com/products/docker-desktop) – For building and running the Docker container.
- [Git](https://git-scm.com/) – For pulling the code from GitHub.

## 🏗 Setup Instructions

### 1️. Clone the Repository

Clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/aaronbau1/job-posting-api.git
cd govify-job-api
```

### 2. Build the Docker Image
```bash
docker build -t job-posting-api .
```

### 3. Run the Docker Image
```bash
docker run -d -p 8000:8000 job-posting-api
```

### 4. Access the Application
The api will be available at http://localhost:8000 on your machine. 

### 5. Documentation for API endpoints
API documentation can be found at http://localhost:8000/docs
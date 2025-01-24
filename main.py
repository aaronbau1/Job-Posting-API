from fastapi import FastAPI, HTTPException
from models import JobCreate, JobResponse, ApplicantCreate, ApplicantResponse
from job_manager import JobManager
from typing import List, Optional

# Create a FastAPI instance
app = FastAPI()

# Create JobManager Instance
job_manager = JobManager()

# Job endpoints

@app.get("/jobs", response_model=List[JobResponse])
def list_jobs():
    jobs = job_manager.get_jobs()
    return jobs

@app.post("/jobs", response_model=JobResponse)
def create_job_endpoint(job: JobCreate):
    new_job = job_manager.create_job(job.title)
    return new_job

@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job_endpoint(job_id: int):
    job = job_manager.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job Posting {job_id} cannot be found")
    return job

# Applicant Endpoints

@app.post("/applicants", response_model=ApplicantResponse)
def create_applicant_endpoint(applicant: ApplicantCreate):
    new_applicant = job_manager.create_applicant(applicant.name, applicant.job_id)
    if not new_applicant:
        raise HTTPException(status_code=400, detail=f"Job Posting {applicant.job_id} does not exist.")
    return new_applicant

@app.get("/jobs/{job_id}/applicants", response_model=List[ApplicantResponse])
def list_applicants_for_job(job_id: int):
    applicants = job_manager.get_applicants_for_job(job_id)
    if not applicants:
        raise HTTPException(status_code=404, detail=f"No applicants found for Job Posting {job_id}.")
    return applicants
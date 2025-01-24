from pydantic import BaseModel, Field, field_validator

# Jobs API model
class JobCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=40, description="Title of the job posting must be between 1 and 40 characters")
    @field_validator('title')
    def check_non_whitespace(cls, v):
        if not v.strip():
            raise ValueError('Job title must have valid characters')
        return v

class JobResponse(BaseModel):
    id: int
    title: str
    status: str = "open"

# Applicant API model
class ApplicantCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=40, description="Applicant's name must be between 1 and 40 characters")
    @field_validator('name')
    def check_non_whitespace(cls, v):
        if not v.strip():
            raise ValueError('Applicant name must have valid characters')
        return v
    job_id: int

class ApplicantResponse(BaseModel):
    id: int
    name: str
    job_id: int

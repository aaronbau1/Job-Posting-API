class JobManager:
    def __init__(self):
        self.job_id_counter = 0
        self.applicant_id_counter = 0
        self.jobs = {}
        self.applicants = {}

    def create_job(self, title: str):
        self.job_id_counter += 1
        job = {"id": self.job_id_counter, "title": title, "status": "open"}
        self.jobs[self.job_id_counter] = job
        return job

    def get_jobs(self):
        return list(self.jobs.values())

    def get_job(self, job_id: int):
        return self.jobs.get(job_id)

    def create_applicant(self, name: str, job_id: int):
        # Job ID is invalid
        if job_id not in self.jobs:
            return None
        self.applicant_id_counter += 1
        applicant = {"id": self.applicant_id_counter, "name": name, "job_id": job_id}
        self.applicants[self.applicant_id_counter] = applicant
        return applicant

    def get_applicants_for_job(self, job_id: int):
        return [a for a in self.applicants.values() if a["job_id"] == job_id]
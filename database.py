from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))

    return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :id"),
            {"id": id}   
        )
        rows = result.all()
        if len(rows) == 0:
            return None
        return dict(rows[0]._mapping)

def add_application_to_db(job_id, data):
    with engine.begin() as conn:  
        query = text("""
            INSERT INTO applications 
            (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) 
            VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
        """)
        conn.execute(query, {
            "job_id": job_id,
            "full_name": data.get('full_name'),
            "email": data.get('email'),
            "linkedin_url": data.get('linkedin_url'),
            "education": data.get('education'),
            "work_experience": data.get('work_experience'),
            "resume_url": data.get('resume_url')
        })

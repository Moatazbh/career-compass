from datetime import datetime
from bs4 import BeautifulSoup

def clean_html(html_text):
    if not html_text:
        return None
    
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text(separator=" ", strip=True)
        




def normalize_arbeitnow_jobs(raw_jobs):

    normalized_jobs = []

    for job in raw_jobs:
        normalized_job = {
            'title': job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "link": job.get("url"),
            "date": datetime.fromtimestamp(job.get('created_at')).strftime("%y-%m-%d") if job.get('created_at') else None,
            "description": clean_html(job.get("description")),
            "remote": job.get("remote"),
            "tags": job.get("tags"),
            "job_types": job.get("job_types"),
            "source": "arbeitnow"
        }
        normalized_jobs.append(normalized_job)


    return normalized_jobs
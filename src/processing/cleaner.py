def clean_jobs(raw_jobs):
    cleaned_jobs = []
    seen = set()

    for job in raw_jobs:
        cleaned_job = {}

        for key, value in job.items():
            if isinstance(value, str):
                value = value.strip()

            
            if value == "":
                value = None

            cleaned_job[key] = value

        
        unique_key = (
            cleaned_job.get('title'),
            cleaned_job.get('company'),
            cleaned_job.get('location'),
            cleaned_job.get('link')
        )

        if unique_key not in seen:
            seen.add(unique_key)
            cleaned_jobs.append(cleaned_job)

    return cleaned_jobs
SKILLS = ["Python",
    "SQL",
    "Excel",
    "Google Sheets",
    "Power BI",
    "Tableau",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "JavaScript",
    "React",
    "HTML",
    "CSS",
    "API",
    "Automation",
    "Web Scraping",
    "BeautifulSoup",
    "Playwright",
    "Selenium",
    "Docker",
    "AWS",
    "Azure",
    "Git",
    "GitHub",
    "Machine Learning",
    "Data Analysis",
    "Data Visualization"]

def extract_skills_from_text(text):
    found_skills = []

    if not text:
        return found_skills
    
    text_lower = text.lower()

    for skill in SKILLS:
        skill_lower = skill.lower()

        if skill_lower in text_lower:
            found_skills.append(skill)

    return found_skills



def add_skills_to_jobs(jobs):
    jobs_with_skills = []

    for job in jobs:
        description = job.get("description")
        detected_skills = extract_skills_from_text(description)
        job['skills'] = detected_skills
        jobs_with_skills.append(job)

    return jobs_with_skills



def count_skills(jobs):
    skills_counted = {}

    for job in jobs:
        skills = job.get('skills', [])

        for skill in skills:
            if skill not in skills_counted:
                skills_counted[skill] = 1
            else:
                skills_counted[skill] += 1

    return skills_counted

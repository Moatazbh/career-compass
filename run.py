#from src.scraper.job_scraper import scrape_fake_jobs  
#from src.processing.cleaner import clean_jobs
from src.utils import save_jobs_to_csv, save_jobs_to_json, save_top_items_to_csv
from src.processing.analyzer import count_by_field, get_top_items
from src.api.arbeitnow_api import fetch_arbeitnow_data
from src.processing.normalizer import normalize_arbeitnow_jobs
from src.analysis.skill_extractor import add_skills_to_jobs, count_skills


def print_report(title, items):
    print(f"\n{title}")
    print("-" * len(title))
    for item, count in items:
        print(f"{item}: {count}")

def print_data_summary(jobs):
    total_jobs = len(jobs)
    jobs_with_titles = 0
    jobs_with_companies = 0
    jobs_with_locations = 0
    jobs_with_descriptions = 0
    jobs_with_skills = 0

    for job in jobs:
        if job.get("title"):
            jobs_with_titles += 1
        if job.get("company"):
            jobs_with_companies += 1
        if job.get("location"):
            jobs_with_locations += 1
        if job.get("description"):
            jobs_with_descriptions += 1
        if job.get("skills"):
            jobs_with_skills += 1

    print("\nData Summary:")
    print(f"Jobs with titles: {jobs_with_titles}")
    print(f"Jobs with companies: {jobs_with_companies}")
    print(f"Jobs with locations: {jobs_with_locations}")
    print(f"Jobs with descriptions: {jobs_with_descriptions}")
    print(f"Jobs with skills: {jobs_with_skills}")


def print_project_summary(total_jobs):
    print("\nCareer Compass Summary")
    print("----------------------")
    print("Career Compass analyzes job market data to find useful career insights.")
    print(f"Jobs analyzed: {total_jobs}")
    print("Reports created:")
    print("- Top skills")
    print("- Top companies")
    print("- Top locations")
    print("- Top job titles")

def main():

    raw_jobs = fetch_arbeitnow_data()
    normalized_jobs = normalize_arbeitnow_jobs(raw_jobs)
    jobs_with_skills = add_skills_to_jobs(normalized_jobs)
    print_data_summary(jobs_with_skills)
    skills_count = count_skills(jobs_with_skills)
    top_skills = get_top_items(skills_count, 5)
    company_counts = count_by_field(jobs_with_skills, "company")
    top_companies = get_top_items(company_counts, 5)
    location_counts = count_by_field(jobs_with_skills, "location")
    top_locations = get_top_items(location_counts, 5)
    title_counts = count_by_field(jobs_with_skills, "title")
    top_titles = get_top_items(title_counts, 5)



    save_top_items_to_csv(
    top_skills,
    "data/reports/top_skills.csv",
    ["skill", "count"]
)
    save_jobs_to_json(normalized_jobs, "data/cleaned/arbeitnow_jobs_cleaned.json")
    save_jobs_to_csv(
        normalized_jobs,
        "data/cleaned/arbeitnow_jobs_cleaned.csv",
        ["title", "company", "location", "link", "date", "description", "remote", "tags", "job_types", "source", "skills"]
    )



    save_top_items_to_csv(top_skills, "data/reports/top_skills.csv", ["skill", "count"])
    save_top_items_to_csv(top_companies, "data/reports/top_companies.csv", ["company", "count"])
    save_top_items_to_csv(top_locations, "data/reports/top_locations.csv", ["location", "count"])
    save_top_items_to_csv(top_titles, "data/reports/top_titles.csv", ["title", "count"])
    

    print_project_summary(len(jobs_with_skills))

    print("\nCareer Compass pipeline completed successfully!")
    print("Files created:")
    print("- data/cleaned/arbeitnow_jobs_cleaned.json")
    print("- data/cleaned/arbeitnow_jobs_cleaned.csv")
    print("- data/reports/top_skills.csv")
    print("- data/reports/top_companies.csv")
    print("- data/reports/top_locations.csv")
    print("- data/reports/top_titles.csv")



    #jobs = scrape_fake_jobs()
    #cleaned_jobs = clean_jobs(jobs)


    #title_counts = count_by_field(cleaned_jobs, "title")
    #top_titles = get_top_items(title_counts, 5)
    #company_counts = count_by_field(cleaned_jobs, "company")
    #top_companies = get_top_items(company_counts, 5)
    #location_counts = count_by_field(cleaned_jobs, "location")
    #top_locations = get_top_items(location_counts, 5)



    #save_jobs_to_json(cleaned_jobs, "data/cleaned/jobs_cleaned.json")
    #save_jobs_to_csv(
        #cleaned_jobs,
        #"data/cleaned/jobs_cleaned.csv",
        #["title", "company", "location", "link", "detail_title", "date", "description"]
    
    #if cleaned_jobs:
        #print('First Cleaned Job:', cleaned_jobs[0])

        #print("\nTop Job Titles:")
        #print(top_titles)

        #print("\nTop Companies:")
        #print(top_companies)

        #print("\nTop Locations:")
        #print(top_locations)
    





if __name__ == '__main__':
    main()
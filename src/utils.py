import json
import csv
import os


def save_jobs_to_json(jobs, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(jobs, file, indent=4)

def save_jobs_to_csv(jobs, file_path, fieldnames):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for job in jobs:
             job_copy = job.copy()

             skills = job_copy.get('skills', [])
             job_copy['skills'] = ' | '.join(skills)
             writer.writerow(job_copy)

def save_top_items_to_csv(items, file_path, headers):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow(headers)


                for item_name, count in items:
                    writer.writerow([item_name, count])




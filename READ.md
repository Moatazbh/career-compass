# Career Compass

Career Compass is a Python data project that analyzes real job market data and identifies useful career insights such as top skills, companies, locations, and job titles.

The project fetches job data from the Arbeitnow API, cleans and normalizes the data, extracts technical skills from job descriptions, and saves both cleaned datasets and summary reports.

## Project Goals

The goal of this project is to practice and demonstrate skills in:

- API data collection
- Data cleaning
- HTML text cleaning
- Skill extraction from job descriptions
- Python data analysis
- CSV and JSON file exports
- Building a clean project pipeline

## What the Project Does

Career Compass currently:

1. Fetches real job data from the Arbeitnow API.
2. Normalizes the raw job data into a consistent format.
3. Cleans HTML from job descriptions.
4. Extracts technical skills from descriptions.
5. Saves cleaned job data as JSON and CSV.
6. Creates summary reports for:
   - Top skills
   - Top companies
   - Top locations
   - Top job titles

## Earlier Version

An earlier version of this project used Playwright to scrape fake Python job listings for practice. The compact portfolio version now uses the Arbeitnow API for real job data.

## Project Structure

```text
Career Compass/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── reports/
│
├── src/
│   ├── api/
│   │   └── arbeitnow_api.py
│   │
│   ├── processing/
│   │   └── normalizer.py
│   │
│   ├── analysis/
│   │   ├── analyzer.py
│   │   └── skill_extractor.py
│   │
│   └── utils.py
│
├── run.py
└── README.md



## Earlier Version

An earlier version of this project used Playwright to scrape fake Python job listings for practice. The compact portfolio version now uses the Arbeitnow API for real job data.
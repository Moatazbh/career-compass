from src.scraper.browser import close_browser, start_browser
from src.utils import save_jobs_to_csv, save_jobs_to_json

def scrape_fake_jobs():
    playwright, browser, page = start_browser(headless=False)
    page.goto("https://realpython.github.io/fake-jobs/")
    page.wait_for_timeout(3000)
    print(page.title())
    job_cards = page.locator('div.card-content')

    jobs = []
    for i in range(job_cards.count()):
        card = job_cards.nth(i)
        title = card.locator('h2.title').inner_text()
        company = card.locator('h3.subtitle').inner_text()
        location = card.locator('p.location').inner_text()
        link = card.locator('a', has_text='Apply').get_attribute('href')
        detail_page = browser.new_page()
        detail_page.goto(link)
        detail_page_title= detail_page.locator('h1.is-2').inner_text()
        date = detail_page.locator('p#date').inner_text()
        description = detail_page.locator('div.content > p').first.inner_text()
        job = {
            'title': title, 
            'company': company,
            'location': location,
            'link': link,
            'detail_title': detail_page_title,
            'date': date, 
            'description': description
        }
        jobs.append(job)
        detail_page.close()


    save_jobs_to_json(jobs, 'data/raw/jobs.json')
    save_jobs_to_csv(jobs, 'data/raw/jobs.csv', ["title", "company", "location", "link", "detail_title", "date", "description"])
    


    print(jobs[0])    
    print('Total jobs collected:', len(jobs))
    print('Saved Jobs to data/raw/jobs.json')
    print('Saved Jobs to data/raw/jobs.csv')

    close_browser(playwright, browser)
    return jobs

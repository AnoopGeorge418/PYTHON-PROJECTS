import os
import requests
import csv
from bs4 import BeautifulSoup

# Constants
URL = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=data+Scientist&txtLocation=&cboWorkExp1=0'
SCRAPER_DIR = input('Enter Folder name to store job details: ')

# Fetch the HTML content from the URL
def fetch_content(url):
    response = requests.get(url)
    return response.text

# Parse the HTML content using BeautifulSoup
def parse_content(content):
    soup = BeautifulSoup(content, 'lxml')
    return soup

# Get unfamiliar skills from the user
def get_unfamiliar_skills():
    print('Enter the skills that you are not familiar with:')
    return input('>')

# Get filename from the user
def get_filename():
    print('Enter the file name for the data to get store (without extension):')
    return input('>')

# Find jobs and filter them based on unfamiliar skills
def find_jobs(soup, unfamiliar_skills):
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    job_list = []

    for job in jobs:
        published_date = job.find('span', 'sim-posted').text.strip()
        if 'few' in published_date:
            company_name = job.find('h3', 'joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            for_more_info = job.header.h2.a['href']

            if unfamiliar_skills not in skills:
                job_list.append({
                    'Company Name': company_name,
                    'Required Skills': skills,
                    'More Info': for_more_info
                })

    return job_list

# Save job posts to a CSV file
def save_to_csv(job_list, filename):
    file_path = os.path.join(SCRAPER_DIR, f'{filename}.csv')
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Company Name', 'Required Skills', 'More Info'])
        writer.writeheader()
        writer.writerows(job_list)

# Save job posts to a TXT file
def save_to_txt(job_list, filename):
    file_path = os.path.join(SCRAPER_DIR, f'{filename}.txt')
    with open(file_path, 'w') as file:
        for index, job in enumerate(job_list):
            file.write(f'Job {index + 1}\n')
            file.write(f'----------------------------------------\n\n')
            file.write(f'Company Name: {job["Company Name"]}\n')
            file.write(f'Required Skills: {job["Required Skills"]}\n')
            file.write(f'More Info: {job["More Info"]}\n')
            file.write(f'----------------------------------------\n\n')

# Main function to run the script
def main():
    os.makedirs(SCRAPER_DIR, exist_ok=True)

    unfamiliar_skills = get_unfamiliar_skills()
    filename = get_filename()

    content = fetch_content(URL)
    soup = parse_content(content)
    job_list = find_jobs(soup, unfamiliar_skills)

    save_to_txt(job_list, filename)

    print(f'Jobs saved to {filename}.txt and {filename}.csv in the {SCRAPER_DIR} directory.')

# Entry point of the script
if __name__ == '__main__':
    main()
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("List Of Jobs in India (Monster.com Indeed.co.in)")
search=input("Enter Job Title: ")
print("==============================")

#Monster.com
url1 = "https://www.monster.com/jobs/search/?q="+search.replace(" ","-")+"&where=india&stpage=1&page=10"
html1 = urllib.request.urlopen(url1, context=ctx).read()
soup1 = BeautifulSoup(html1, 'html.parser')
results1 = soup1.find(id='ResultsContainer')
job_elems = results1.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(title_elem.find('a')['href'])
    print()

print("==============================\n")

#Indeed.co.in
n="0"
while True:
    url2="https://www.indeed.co.in/jobs?q="+search.replace(" ","+")+"&start="+n
    html2 = urllib.request.urlopen(url2, context=ctx).read()
    soup2 = BeautifulSoup(html2,'html.parser')
    results2 = soup2.find(id='resultsCol')
    job_elems = results2.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result')
    for job_elem in job_elems:
        title_elem = job_elem.find('a', class_='jobtitle turnstileLink ')['title']
        company_elem = job_elem.find('span', class_='company')
        location_elem = job_elem.find('span', class_='location accessible-contrast-color-location')
        salary= job_elem.find('span', class_='salaryText')
        link = job_elem.find('a', class_='jobtitle turnstileLink ')['href']
        if None in (title_elem, company_elem, location_elem, link, salary):
            continue
        print(title_elem.strip())
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print(salary.text.strip())
        print("https://www.indeed.co.in"+link)
        print()
    n=str(int(n)+10)
    q=input("Continue for more? y/n: ")
    if q=='n':
        break
    print()

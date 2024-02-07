import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint
headers_generator = Headers(os='win', browser='chrome')

response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=headers_generator.generate())
main_html_data = response.text
main_soup = BeautifulSoup(main_html_data, features='lxml')

vacancy_list_tag = main_soup.find('div', id='a11y-main-content')
vacancy_list = vacancy_list_tag.find_all('div', class_='serp-item serp-item_link')

result_list = []
print(len(vacancy_list))
for vacancy in vacancy_list:
    link_vacancy_tag = vacancy.find('a', class_='bloko-link')
    link_vacancy = link_vacancy_tag['href']

    name_vacancy_tag = link_vacancy_tag.find('span', class_='serp-item__title')
    name_vacancy = name_vacancy_tag.text

    fork_vacancy_tag = vacancy.find('span', 'bloko-header-section-2')
    if fork_vacancy_tag:
        fork_vacancy = fork_vacancy_tag.text
    else:
        fork_vacancy = None

    company_city_tag = vacancy.find('div', class_='vacancy-serp-item__info')
    company_city = company_city_tag.find_all('div', class_='bloko-text')
    city_vacancy = company_city[1].text
    company_vacancy = company_city[0].text

    response = requests.get(link_vacancy, headers=headers_generator.generate())
    html_data = response.text

    soup = BeautifulSoup(html_data, features='lxml')

    keywords_vacancy_tag = soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text')

    keywords_vacancy_list = []

    for keywords_vacancy in keywords_vacancy_tag:
        keywords_vacancy_list.append(keywords_vacancy.text)

    if 'Django' not in keywords_vacancy_list and 'Flask' not in keywords_vacancy_list:
        continue

    result_list.append({
        'name_vacancy': name_vacancy,
        'link_vacancy': link_vacancy,
        'fork_vacancy': fork_vacancy,
        'city_vacancy': city_vacancy,
        'company_vacancy': company_vacancy
    })

print(result_list)









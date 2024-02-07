from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options


def wait_element(browser, delay_second=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_second).until(
        expected_conditions.presence_of_element_located((by, value))
    )


# Устанавливает драйвер для selenium Chrome браузера и возвращает путь
chrome_webdriver_path = ChromeDriverManager().install()
# Экземпляр клаcса Service
browser_service = Service(executable_path=chrome_webdriver_path)
# Создаем опцию скрытия браузера
options = Options()
options.add_argument('--headless')
# Создаем браузер (нужен сам браузер!)
browser = Chrome(service=browser_service)
# Открываем сайт
browser.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2')
# Ищем все тэги статей
vacancies_list_tag = wait_element(browser, by=By.ID, value='a11y-main-content')
vacancies_list = vacancies_list_tag.find_elements(By.CLASS_NAME, 'vacancy-serp-item-body__main-info')

links_list = []

for vacancy in vacancies_list:
    links_vacancy_tag = wait_element(vacancy, by=By.CLASS_NAME, value='serp-item__title-link-wrapper')
    links_vacancy = wait_element(links_vacancy_tag, by=By.TAG_NAME, value='a')
    link_vacancy = links_vacancy.get_attribute('href')
    links_list.append(link_vacancy)

    name_vacancy_tag = wait_element(links_vacancy_tag, by=By.TAG_NAME, value='span')
    name_vacancy = name_vacancy_tag.text.strip()

    fork_vacancy_tag = wait_element(vacancy, by=By.CLASS_NAME, value='vacancy-serp-item__layout')
    print(fork_vacancy_tag)


for link in links_list:
    browser.get(link)

    keywords_vacancy_tag = wait_element(browser, by=By.CLASS_NAME, value='bloko-tag bloko-tag_inline')

keywords_list = []

browser.get(links_list[0])
keywords_vacancy_tag = wait_element(browser, by=By.CLASS_NAME, value='bloko-tag-list')
keywords_vacancy_list = keywords_vacancy_tag.find_elements(by=By.TAG_NAME, value='span')

for keywords_vacancy in keywords_vacancy_list:
    keyword_vacancy = keywords_vacancy.text
    keywords_list.append(keyword_vacancy)

    if 'Django' not in keywords_vacancy_list and 'Flask' not in keywords_vacancy_list:
        continue



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


chrome_webdriver_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_webdriver_path)
browser = Chrome(service=browser_service)
browser.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2')
vacancies_list_tag = wait_element(browser, by=By.ID, value='a11y-main-content')
vacancies_list = vacancies_list_tag.find_elements(By.CLASS_NAME, 'vacancy-serp-item-body__main-info')
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.common.keys import Keys
from Constants import ui_URL


@allure.description("Тестирование поля поиска по названию и автору на сайте Читай-город.")

class Search:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get(ui_URL)

    @allure.step("Поиск книги по названию")
    def search_book_title(self, book_title):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name='phrase']").send_keys(
            book_title, Keys.RETURN)


    @allure.step("Поиск книги по автору")
    def search_book_author(self, book_author):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name='phrase']").send_keys(
            book_author, Keys.RETURN)        
        
    
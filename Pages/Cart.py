from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.common.keys import Keys
from Constants import ui_URL


@allure.description("Тестирование добавления, редактирования и удаления товара в корзине на сайте Читай-город.")
class Cart:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get(ui_URL)

    @allure.step("Поиск книги по автору и переход на страницу книги")
    def search_book_title(self, book_author):
        self.driver.find_element(
            By.CSS_SELECTOR, "[name='phrase']").send_keys(
            book_author, Keys.RETURN)

    @allure.step("Переход на страницу книги")
    def product_card(self):
        self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/a[1]/picture[1]/img[1]").click()

    @allure.step("Добавление книги в корзину")
    def add_to_cart(self):
        self.driver.find_element(
            By.XPATH,
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()

    @allure.step("Удаление книги из корзины")
    def delete_from_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".cart-item__actions-icon").click()



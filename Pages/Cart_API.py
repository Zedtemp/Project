import requests
import json
import allure
from Constants import api_URL1, api_URL2, access_token


@allure.description("API Тестирование добавления, редактирования и удаления товара в корзине на сайте Читай-город ..")
class CartAPI:

    url1 = api_URL1
    url2 = api_URL2

    def __init__(self, url):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': access_token
        }

    @allure.step("Добавление книги в корзину через id")
    def add_to_cart(self, book_id: int) -> str:
        data = {
            "id": book_id,
        }
        resp = requests.post(
            self.url1, headers=self.headers, data=json.dumps(data))
        return resp.status_code
    
    @allure.step("Получение списка товаров в корзине")
    def get_cart(self) -> dict:

        resp = requests.get(self.url2, headers=self.headers)
        return resp.status_code

    @allure.step("Очистка корзины")
    def clear_cart(self):
        resp = requests.delete(self.url2, headers=self.headers)
        return resp.status_code

    @allure.step("Изменение количества товара в корзине")
    def update_cart(self, products: dict) -> tuple:
        response = requests.put(
            self.url2, headers=self.headers, data=json.dumps(products))
        return response.status_code

    @allure.step("Отправка пустого запроса на добавление товара в корзину")
    def add_empty_request(self, book_id: int) -> str:
        resp = requests.post(
            self.url1, json={}, headers=self.headers)
        return resp.status_code
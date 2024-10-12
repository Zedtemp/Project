from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from Pages.Search import Search
from Pages.Cart import Cart

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'


@allure.title("Позитивный тест поиска книг по названию")
@allure.description("Тестирование работоспособности поиска по названию.")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_search_by_title():

    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome(options=options)
        driver.maximize_window
        search = Search(driver)
        driver.implicitly_wait(10)

    with allure.step("Выполнить поиск книги по названию"):
        search.search_book_title("Гарри Поттер")

    with allure.step("Получить результаты поиска"):
        result = driver.find_element(By.CSS_SELECTOR, "article")

    with allure.step("Проверить, что поиск по названию дает не пустой результат"):
        assert result is not None

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Позитивный тест поиска книг по автору")
@allure.description("Тестирование работоспособности поиска по автору.")
@allure.feature("READ")
@allure.severity("CRITICAL")
def test_search_by_author():

    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome(options=options)
        driver.maximize_window
        search = Search(driver)
        driver.implicitly_wait(10)

    with allure.step("Выполнить поиск книги по автору"):
        search.search_book_author("Джоан Роулинг")

    with allure.step("Получить результаты поиска"):
        result = driver.find_element(By.CSS_SELECTOR, "article")

    with allure.step("Проверить, что поиск по автору дает не пустой результат"):
        assert result is not None

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Позитивный тест добавления товара в корзину")
@allure.description("Тестирование работоспособности добавления товара из результатов поиска в корзину.")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_add_cart():
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome(options=options)
        driver.maximize_window
        cart = Cart(driver)
        driver.implicitly_wait(10)

    with allure.step("Выполнить поиск книги по названию"):
        driver.implicitly_wait(10)
        cart.search_book_title("Гарри Поттер")

    with allure.step("Перейти на страницу книги"):
        cart.product_card()

    with allure.step("добавить книгу в корзину"):
        cart.add_to_cart()
        result = driver.find_element(By.CSS_SELECTOR, ".products")

    with allure.step("Проверить, что в корзине не пусто"):
        assert result is not None

    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title("Позитивный тест удаления товара из корзины")
@allure.description("Тестирование удаления товара из корзины.")
@allure.feature("DELETE")
@allure.severity("BLOCKER")
def test_delete_cart():
    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome(options=options)
        driver.maximize_window
        cart = Cart(driver)
        driver.implicitly_wait(10)

    with allure.step("Выполнить поиск книги по названию"):
        cart.search_book_title("Гарри Поттер")

    with allure.step("Перейти на страницу книги"):
        cart.product_card()

    with allure.step("Добавить книгу в корзину"):
        cart.add_to_cart()

    with allure.step("Удалить книгу из корзины"):
        cart.delete_from_cart()
        result = driver.find_element(
            By.XPATH, "//div[@class='empty-title']").text

    with allure.step("Проверить, что в корзине пусто"):
        assert result == "В корзине ничего нет"


@allure.title("Негативный тест поиска книг по названию")
@allure.description("Тестирование поиска по некорректному(несуществующему) названию.")
@allure.feature("READ")
@allure.severity("MAJOR")
def test_search_by_incorrect_title():

    with allure.step("Запустить браузер Chrome"):
        driver = webdriver.Chrome(options=options)
        driver.maximize_window
        search = Search(driver)
        driver.implicitly_wait(10)

    with allure.step("Выполнить поиск книги по названию"):
        search.search_book_title("qwertyuio")

    with allure.step("Получить результаты поиска"):
        result_text = driver.find_element(
            By.CSS_SELECTOR, ".catalog-empty-result__header").text
    with allure.step("Проверить, что поиск дает пустой результат и соответствующий текст"):
        assert result_text == "Похоже, у нас такого нет"

    with allure.step("Закрыть браузер"):
        driver.quit()

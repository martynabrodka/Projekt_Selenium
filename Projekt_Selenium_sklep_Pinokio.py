# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

# DANE TESTOWE

#użytkownik niezalogowany
number1 = "20000"
number2 = "2"
size1 = "68"
size2 = "74"
country_name = "Albania"

class BuyingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://pinokio.pl")
        self.driver.implicitly_wait(6)

    def testOver9999(self):
        # KROKI
        driver = self.driver
        driver.delete_all_cookies()
        # 1. Kliknij "Dziewczynka"
        driver.find_element(By.PARTIAL_LINK_TEXT, "Dziewczynka").click()
        # Poczekaj max 6 s na załadowanie strony
        driver.set_page_load_timeout(6)
        # 2. Wybierz produkt "Spódnica jeans Romantic"
        product = driver.find_element(By.PARTIAL_LINK_TEXT, "Spódnica Jeans Romantic")
        product.click()
        # 3. Wybierz dowolny rozmiar. Wybieram rozmiar 68
        size1 = driver.find_element(By.PARTIAL_LINK_TEXT, "68")
        size1.click()
        # 4. Wyczyść okno Ilość
        amount = driver.find_element(By.ID, 'UserCartQuantity')
        amount.click()
        amount.send_keys(Keys.CONTROL + "a")
        amount.send_keys(Keys.DELETE)
        # Poczekaj 2s w celu sprawdzenia, co się dzieje w oknie
        sleep(2)
        # 5. Wpisz żądaną liczbę produktów powyżej 9999 sztuk
        amount.send_keys(number1)
        # 6. Zatwierdź produkty w koszyku
        driver.find_element(By.CLASS_NAME, "product-add-cart.btn.btn-primary.btn-lg ").click()
        # 7. Sprawdź, czy pojawia się informacja:"Produkt został dodany do koszyka."
        product_in_cart = driver.find_element(By.XPATH, '//div[@class="message success"]//span').text
        self.assertEqual("Produkt został dodany do koszyka.", product_in_cart)
        sleep(2)
        # 8. Przejdź do koszyka
        driver.find_element(By.PARTIAL_LINK_TEXT, "Przejdź do koszyka").click()
        # 9. Sprawdź, czy pojawia się informacja:"Uwaga! Nie można zamówień więcej niż 9999 sztuk jednego produktu. Produktowi Spódnica Jeans Romantic została zmniejszona ilość w koszyku."
        warning_message = driver.find_element(By.XPATH, '//div[@class="message info"]//span').text
        self.assertEqual("Uwaga! Nie można zamówień więcej niż 9999 sztuk jednego produktu. Produktowi Spódnica Jeans Romantic została zmniejszona ilość w koszyku.", warning_message)
        # 10. Sprawdź, czy w Twoim Koszyku została zmniejszona ilość produktów do 9999 sztuk
        amount_in_cart = driver.find_element(By.ID, "UserCart0Quantity").get_attribute("value")
        self.assertTrue("9999", amount_in_cart)
        sleep(3)
        print("Test Over 9999 - OK")
    def testOutsidePoland(self):
        # KROKI
        driver = self.driver
        driver.delete_all_cookies()
        # 1. Kliknij "Dziewczynka"
        driver.find_element(By.PARTIAL_LINK_TEXT, "Dziewczynka").click()
        # Poczekaj max 6 s na załadowanie strony
        driver.set_page_load_timeout(6)
        # 2. Wybierz produkt "Spódnica jeans Romantic"
        product = driver.find_element(By.PARTIAL_LINK_TEXT, "Spódnica Jeans Romantic")
        product.click()
        # 3. Wybierz dowolny rozmiar. Wybieram rozmiar 74
        size2 = driver.find_element(By.PARTIAL_LINK_TEXT, "74")
        size2.click()
        # 4. Wyczyść okno Ilość
        amount = driver.find_element(By.ID, 'UserCartQuantity')
        amount.click()
        amount.send_keys(Keys.CONTROL + "a")
        amount.send_keys(Keys.DELETE)
        # Poczekaj 2s w celu sprawdzenia, co się dzieje w oknie
        sleep(2)
        # 5. Wpisz żądaną liczbę produktów
        amount.send_keys(number2)
        # 6. Zatwierdź produkty w koszyku
        driver.find_element(By.CLASS_NAME, "product-add-cart.btn.btn-primary.btn-lg ").click()
        # 7. Sprawdź, czy pojawia się informacja:"Produkt został dodany do koszyka."
        sleep(2)
        product_in_cart = driver.find_element(By.XPATH, '//div[@class="message success"]//span').text
        self.assertEqual("Produkt został dodany do koszyka.", product_in_cart)
        # 8. Przejdź do koszyka
        driver.find_element(By.PARTIAL_LINK_TEXT, "Przejdź do koszyka").click()
        # 9. Wybierz kraj dostawy inny niż Polska
        find_country = driver.find_element(By.CLASS_NAME, "transform-open")
        # Przescrolluj niżej do docelowego elementu
        driver.execute_script("arguments[0].scrollIntoView()", find_country)
        sleep(5)
        find_country.click()
        fact_country = driver.find_element(By.XPATH, '//input[@class="form-control disable-on-submit"]')
        fact_country.send_keys(country_name)
        driver.find_element(By.PARTIAL_LINK_TEXT, "Albania").click()
        sleep(5)
        # 10. Kliknij "Zamawiam"
        order = driver.find_element(By.CLASS_NAME, "btn-next.btn.btn-primary.btn-lg.btn-block")
        # Przescrolluj niżej do docelowego elementu
        driver.execute_script("arguments[0].scrollIntoView()", order)
        order.click()
        sleep(5)
        # 11. Sprawdź, czy pojawia się komunikat o błędach
        error_message = driver.find_element(By.XPATH, '//div[@class="message error"]//span').text
        self.assertEqual("W Twoim koszyku znajdują się następujące błędy:\nNie wybrano punktu płatności.\nNie można wybrać wybranej formy płatności.\nNie można wybrać wybranej formy dostawy.", error_message)
        sleep(3)
        print("Test Outside Poland - OK")

    def tearDown(self):
        self.driver.quit()
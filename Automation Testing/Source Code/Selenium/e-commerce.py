import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

 

class TestScenarioecomerce(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.mapclub.com")

    def test_ecomerce(self):
        # Implementasi skenario uji 1
        wait = WebDriverWait(self.driver, 60)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/member/login']")))
        self.driver.find_element(By.XPATH, "//a[@href='/member/login']").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']")))
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("#username")

        self.driver.find_element(By.XPATH, "//button[@class='button submit']").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("#password")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'Login')]")))
        self.driver.find_element(By.XPATH, "//button[contains(.,'Login')]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'Create PIN Later')]")))
        self.driver.find_element(By.XPATH, "//a[contains(.,'Create PIN Later')]").click()
        time.sleep(3)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='keyword']")))
        self.driver.find_element(By.XPATH, "//input[@name='keyword']").send_keys("samsung A34")
        self.driver.find_element(By.XPATH, "//input[@name='keyword']").send_keys(Keys.ENTER)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='product-grid__item'][contains(.,'GALAXY A34 5G 8/128GB BLACK')] ")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='/item/samsung/samsung/galaxy-a34-5g-8-128gb-black-SP230914323368-A004'])[3]"))).click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='btn btn-black-border btn-add-shopbag'][contains(.,'ADD TO BAG')]"))).click()


        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='dialog-content']//div//p[contains(.,'ADD TO BAG SUCCESSFULLY')]")))
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='dialog-content']//div//p[contains(.,'ADD TO BAG SUCCESSFULLY')]")))


        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/shoppingcart']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@class='shopping-cart__list-product']//a[contains(.,'GALAXY A34 5G 8/128GB BLACK')] ")))

        element_to_hover_over= self.driver.find_element(By.XPATH, "(//li[@class='shopping-cart__list-product'][contains(.,'GALAXY A34 5G 8/128GB BLACK')]//a)[5]")
        action = ActionChains(self.driver)
        action.move_to_element(element_to_hover_over).perform()

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//li[@class='shopping-cart__list-product'][contains(.,'GALAXY A34 5G 8/128GB BLACK')]//a)[5]"))).click()
        # breakpoint()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'DELETE')]")))
        self.driver.find_element(By.XPATH, "//a[contains(.,'DELETE')]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[contains(.,'You don’t have anything in your bag yet.')]")))


    def tearDown(self):
        self.driver.quit()

    
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(TestScenarioecomerce))


if __name__ == "__main__":
    unittest.TextTestRunner().run(test_suite)
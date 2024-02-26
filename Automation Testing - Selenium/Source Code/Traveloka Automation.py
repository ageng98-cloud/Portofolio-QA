import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

 

class TestTraveloka(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.traveloka.com/en-id")

    def test_trveloka(self):
        
        wait = WebDriverWait(self.driver, 60)
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n r-1pi2tsx r-bnwqim r-184en5c'][contains(.,'Car Rental')]")))
        self.driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1pi2tsx r-bnwqim r-184en5c'][contains(.,'Car Rental')]").click()
        
        time.sleep(2)
        
        #Pick-up Location 
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter city or region']")))
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter city or region']").send_keys("jakarta")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Jakarta']//div")))
        self.driver.find_element(By.XPATH, "//div[@aria-label='Jakarta']//div").click()

        time.sleep(3)

        #Pick-up Date Rental Start Date
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[3]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[3]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@data-testid='date-marker-today'])[1]")))
        self.driver.find_element(By.XPATH, "(//div[@data-testid='date-marker-today'])[1]").click()

        time.sleep(3)

        #Pickup Time Rental Start Date

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[4]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[4]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-xyw6el']//div[contains(.,'2')])[5]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-xyw6el']//div[contains(.,'2')])[5]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-y46g1k']//div[contains(.,'Done')])[1]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-y46g1k']//div[contains(.,'Done')])[1]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='02:00']")))
        

        #Pick-up Date Rental End Date
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[5]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[5]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@data-testid='date-marker-today'])[1]")))
        self.driver.find_element(By.XPATH, "(//div[@data-testid='date-marker-today'])[1]").click()

        time.sleep(3)

        #Pickup Time Rental End Date
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[6]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[6]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-xyw6el']//div[contains(.,'10')])[5]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-xyw6el']//div[contains(.,'10')])[5]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-y46g1k']//div[contains(.,'Done')])[1]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-y46g1k']//div[contains(.,'Done')])[1]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='10:00']")))

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='rental-search-form-cta']")))
        self.driver.find_element(By.XPATH, "//div[@data-testid='rental-search-form-cta']").click()

        #Check Header Result Search Content
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n r-391gc0 r-kdyh1x'][contains(.,'Car Rental Without Driver')][contains(.,'Jakarta')][contains(.,'Tue, 20 Feb 2024 02:00')][contains(.,'Tue, 20 Feb 2024 10:00')]")))


    def tearDown(self):
        self.driver.quit()

    
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(TestTraveloka))


if __name__ == "__main__":
    unittest.TextTestRunner().run(test_suite)
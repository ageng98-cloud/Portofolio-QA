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
        
        #Select tab Without Driver
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n r-1h84pjw r-jwli3a r-1e081e0 r-5njf8e'][contains(.,'Without Driver')]")))
        self.driver.find_element(By.XPATH, "//div[@class='css-1dbjc4n r-1h84pjw r-jwli3a r-1e081e0 r-5njf8e'][contains(.,'Without Driver')]").click()

        #Pick-up Location 
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter city or region']")))
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter city or region']").send_keys("jakarta")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Jakarta']//div")))
        self.driver.find_element(By.XPATH, "//div[@aria-label='Jakarta']//div").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Jakarta']")))
        

        #Pick-up Date Rental Start Date
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[3]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[3]").click()

        startdate= wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1awozwy r-1vjbqqu r-1naam9t r-sdzlij r-d045u9 r-eqz5dr r-16y2uox r-1472mwg r-1777fci r-1wyvozj r-1pn2ns4 r-u8s1d r-70iriu r-136ojw6'])[1]")))
        startdate.click()


        #Pickup Time Rental Start Date

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[4]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[4]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-xyw6el']//div[contains(.,'9')])[5]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-xyw6el']//div[contains(.,'9')])[5]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-y46g1k']//div[contains(.,'Done')])[1]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-y46g1k']//div[contains(.,'Done')])[1]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='09:00']")))
        

        #Pick-up Date Rental End Date
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[5]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[5]").click()
        
        enddate= wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1awozwy r-1vjbqqu r-1naam9t r-sdzlij r-d045u9 r-eqz5dr r-16y2uox r-1472mwg r-1777fci r-1wyvozj r-1pn2ns4 r-u8s1d r-70iriu r-136ojw6'])[2]")))
        enddate.click()

        time.sleep(3)

        #Pickup Time Rental End Date
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[6]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-1kb76zh'])[6]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-xyw6el']//div[contains(.,'11')])[5]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-xyw6el']//div[contains(.,'11')])[5]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-y46g1k']//div[contains(.,'Done')])[1]")))
        self.driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-y46g1k']//div[contains(.,'Done')])[1]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='11:00']")))

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='rental-search-form-cta']")))
        self.driver.find_element(By.XPATH, "//div[@data-testid='rental-search-form-cta']").click()

        #Check Header Result Search Content
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n r-391gc0 r-kdyh1x'][contains(.,'Car Rental Without Driver')][contains(.,'Jakarta')]")))

        car=wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-ymttw5 r-95jzfe'][contains(.,'Toyota')]//div[contains(.,'Continue')])[3]")))
        car.click()

        element_to_scroll = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-nsbfu8'][contains(.,'Jakarta')]//div[contains(.,'Continue')])[3]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
        self.driver.execute_script("window.scrollBy(0, 200);")

        carProvider=wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='css-1dbjc4n r-18u37iz r-nsbfu8'][contains(.,'Jakarta')]//div[contains(.,'Continue')])[3]")))
        carProvider.click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(.,'Toyota')]")))
        time.sleep(3)


    def tearDown(self):
        self.driver.quit()

    
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(TestTraveloka))


if __name__ == "__main__":
    unittest.TextTestRunner().run(test_suite)
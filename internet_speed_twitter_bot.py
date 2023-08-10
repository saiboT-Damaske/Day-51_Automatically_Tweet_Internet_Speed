import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys


class MyUDC(uc.Chrome):
    def __del__(self):
        try:
            self.service.process.kill()
        except:  # noqa
            pass



class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 99
        self.up = 99

        self.driver = MyUDC()
        self.driver.maximize_window()


    def get_internet_speed(self):
        print("testing 1. 2. 1. 2. testing")
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'More Options')]").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Confirm My Choices')]").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".js-start-test").click()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "mobile-test-complete")))
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"Download speed: {self.down}")
        print(f"Upload speed: {self.up}")


    def tweet_at_provider(self, username, password, down_speed, up_speed):

        message = f"Hey Internet Provider, today may download/upload speed was {self.down}/{self.up} Mbps.\n" \
                  f"You promised me {down_speed}/{up_speed} Mbps."

        self.login_gmail(username=username, password=password)
        print("logged into gmail")
        print("now tweet tweet")
        self.driver.get("https://twitter.com")
        sleep(6)
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Refuse non-essential cookies')]/../..").click()
        sleep(2)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@title="Sign in with Google Dialog"]'))
        sleep(2)
        google_sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="continue-as"]')
        print(google_sign_in_button.text)
        print("element found")
        google_sign_in_button.click()
        # --- loading Twitter homepage
        sleep(8)
        self.driver.find_element(By.XPATH, '//*[@class="DraftEditor-editorContainer"]').click()
        sleep(3)
        # --- closing popup
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@class="DraftEditor-editorContainer"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="DraftEditor-editorContainer"]/div/div').send_keys(message)
        sleep(2)
        post_buttons = self.driver.find_elements(By.XPATH, '//span[contains(text(), "Post")]/../..')
        post_buttons[1].click()
        print("post tweeted successfully")
        print(message)
        # hit escape once you select the text field




    def login_gmail(self, username, password):
        self.driver.get('https://accounts.google.com/ServiceLogin')
        sleep(3)

        self.driver.find_element(By.XPATH, '//input[@type="email"]').send_keys(username)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
        sleep(3)

        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys(password)
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
        sleep(4)

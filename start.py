
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()
    
    def login(self):
        #/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input
        self.driver.get("https://www.instagram.com/?hl=en")
        time.sleep(2)
        #login button
        #/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]

        user_name_element = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        user_name_element.clear()
        user_name_element.send_keys(self.username)
        login_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")

        password_element = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        password_element.clear()
        password_element.send_keys(self.password)



bot = InstaBot("Soumalya","blablabla")
bot.login()
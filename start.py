
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import os


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
        password_element.send_keys(Keys.RETURN)
    
    def skip_NotNow_LoginInfo(self):
        #ui.WebDriverWait(self.driver,5).until(EC.element_to_be_clickable( (By.CSS_SELECTOR,".aOOlW.HoLwm") )).click()
        #time.sleep(2)
        ui.WebDriverWait(self.driver,10).until(EC.element_to_be_clickable( (By.CSS_SELECTOR,".aOOlW.HoLwm") )).click()


    def get_boys(self):
        driver = self.driver
        boys = []
        visited = []
        with open("bois.txt","r") as file:
            for row in file:
                boys.append(row)
            
            boy = random.choice(boys)
        
            while boy not in visited:
                boy = random.choice(boys)
                visited.append(boy)
                # search_element = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div")
                # ui.WebDriverWait(self.driver,5).until(EC.element_to_be_clickable( By.XPATH("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div") )).click()
                # #search_element.clear()
                # search_element.send_keys(boy)
                # search_element.send_keys(Keys.RETURN)
                print(str(boy))
                driver.get("https://www.instagram.com/" + str(boy) + "/")
                time.sleep(2)
                break
            
                




bot = InstaBot("the_hypercool_dude","soumalya@10")
bot.login()
bot.skip_NotNow_LoginInfo()

while True:
    temp = input("press y to get another boy:\n press n to exit the system:::: ")
    if temp == 'y':
        bot.get_boys()
    else:
        bot.closeBrowser()
        break
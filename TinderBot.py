from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


bot = webdriver.Chrome()

bot.implicitly_wait(2)
bot.get("https://tinder.com/")

login_button = bot.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

sleep(2)

login_by_phone_button = bot.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button')
login_by_phone_button.click()


number_input_box = bot.find_element_by_name('phone_number')
phone_number = input("Enter phone number: ")
number_input_box.send_keys(f'{phone_number}')
number_input_box.send_keys(Keys.RETURN)


code = str(input("Enter security code: "))

for i in range(len(code)):
    elem = bot.find_element_by_xpath(f'//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[{i+1}]')
    elem.send_keys(f"{code[i]}")

elem.send_keys(Keys.RETURN)

location_permission_button = bot.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location_permission_button.click()


notification_permission_button = bot.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
notification_permission_button.click()


cookie_accept_button = bot.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookie_accept_button.click()

while True:
    try:
        swipe_right_button = bot.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        swipe_right_button.click()
    except NoSuchElementException:
        try: 
            ignore_popup_button = bot.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
            ignore_popup_button.click()
        except Exception:
            close_match_button = bot.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
            close_match_button.click()

            

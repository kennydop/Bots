from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import clipboard

email_address = "dansooffeipatrick@gmail.com"

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://open.spotify.com/?_ga=2.222703323.1562941152.1615326584-1171800429.1615326584")
action = ActionChains(driver)
links = open("track links.txt", "w+")

element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#main > div > div.Root__top-container > div.Root__top-bar > header > div:nth-child(5) > button._3f37264be67c8f40fa9f76449afdb4bd-scss._1f2f8feb807c94d2a0a7737b433e19a8-scss'))
)
element.click()

email_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#login-username'))
)
email_input.send_keys(email_address)

email_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#login-password'))
)
email_input.send_keys("$inevitable55SP")

driver.find_element_by_css_selector("#login-button").click()

element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#main > div > div.Root__top-container > nav > div.e628850198dd4b611f8d7ebc057a4734-scss > div.bbba02db95e363ecc51e2aa98adfd6a6-scss > div > div:nth-child(3) > a > span'))
)
element.click()

driver.implicitly_wait(5)

tracks = driver.find_elements_by_class_name('e8ea6a219247d88aa936a012f6227b0d-scss bddcb131e9b40fa874148a30368d83f8-scss bcc38527b11ab105d496846b4ad11ef4-scss')
print('\n Number of Liked Tracks = ', len(tracks), '\n')
print('\n The Links are \n')

for track in tracks:
    action.context_click(track)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#context-menu-root > ul > li:nth-child(8) > button'))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tippy-87 > ul > li:nth-child(1) > button'))).click()
    link = clipboard.get()
    print(link)
    links.append(link + '\n')

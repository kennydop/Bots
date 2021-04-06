from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

num_scroll = 1000
username = input("Enter account handle: ")
password = input("Enter account password: ")
followed = open("to be unfollowed.txt", "r+")
unfollowed = open("to be unfollowed.txt", "w+")

if username == "":
    username = "trayl_inc"
    num_scroll = 350

if password == "" and username == "trayl_inc":
    password = "$Loops99"
elif password == "" and username == "kennydop":
    password = "thegram83"



def check_if_done():
    if len(unfollowed) < len(followed):
        Again()

def Again():
    driver.refresh()
    followingbtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(3) > a'))
    )
    followingbtn.click()
    driver.implicitly_wait(2)
    fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")

    scroll = 0
    while scroll < (num_scroll-200): # scroll 800 times
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        driver.implicitly_wait(1.5)
        scroll += 1

    driver.implicitly_wait(2)
    followings  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")

    i = 0
    for follow in followings:
        i = i + 1
        follow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a'.format(i)))
        )
        r = follow.text
        for line in followed:
            if r == line:
                print (r, " = ", line)
                unfollowbtn = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button".format(i))
                unfollowbtn.click()
                driver.implicitly_wait(1)
                unfollowed.append(line)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com")

username_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input'))
)
driver.implicitly_wait(0.5)
username_field.clear()
username_field.send_keys(username)

password_field = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
password_field.clear()
password_field.send_keys(password)
driver.implicitly_wait(1)
loginbtn = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
loginbtn.click()

not_now_pop_up = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm'))
)
not_now_pop_up.click()
driver.implicitly_wait(0.5)

driver.get("https://www.instagram.com/" + username)

followingbtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(3) > a'))
    )
followingbtn.click()
driver.implicitly_wait(2)
fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")

scroll = 0
while scroll < num_scroll: # scroll 1000 times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    driver.implicitly_wait(1.5)
    scroll += 1

driver.implicitly_wait(2)
followings  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")

i = 0
for follow in followings:
    i = i + 1
    follow = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[1]/div[2]/div[1]/span/a'.format(i)))
    )
    r = follow.text
    for line in followed:
        if r == line:
            print (r, " = ", line)
            unfollowbtn = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button".format(i))
            unfollowbtn.click()
            driver.implicitly_wait(1)
            unfollowed.append(line)
check_if_done()

followed.close()
unfollowed.close()
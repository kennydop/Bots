from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

num_scroll = 600
username = input("Enter account handle: ")
password = input("Enter account password: ")
target = input("Name of target: ")
# followed = open("to be unfollowed.txt", "w+")

if username == "":
    username = "trayl_inc"
    num_scroll = 250
    
if password == "" and username == "trayl_inc":
    password = "$Loops99"
elif password == "" and username == "kennydop":
    password = "thegram83"

if target == "" and username != "kennydop":
    target = "kennydop"

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

profilepic = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > span > img'))
)

driver.get("https://www.instagram.com/" + target)

followersbtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a'))
    )
followersbtn.click()
driver.implicitly_wait(2)
fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
try:
    scroll = 0
    while scroll < num_scroll: # scroll 600 times
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        driver.implicitly_wait(1.5)
        scroll += 1
    driver.implicitly_wait(2)
    followers  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
    print("followers len is {}".format(len(followers)))

except Exception as e:
    print (e)

i = 0
for follower in followers:
    i = i + 1
    try:
        driver.implicitly_wait(0.5)
        follow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button'.format(i)))
        )
        r = follower.text
        r = r.split()
        rl = (r[-1])
        print(rl)
        if rl == "Follow":
            print(r[0])
            # followed.append(r[0] + '\n')
            follow.click()
            driver.implicitly_wait(0.5)
    except Exception as e:
        print(e)
        continue

# followed.close()
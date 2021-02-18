from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = input("Enter account handle: ")
password = input("Enter account password: ")
target = input("Name of target: ")

if username == "":
    username = "trayl_inc"
if password == "":
    password = "$Loops99"  
if target == "":
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

not_now_pop_up = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm'))
)
not_now_pop_up.click()
driver.implicitly_wait(0.5)

driver.get("https://www.instagram.com/" + target)

followersbtn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a'))
    )
followersbtn.click()
driver.implicitly_wait(2)
fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
scroll = 0
while scroll < 400: # scroll 400 times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    driver.implicitly_wait(1.5)
    scroll += 1
driver.implicitly_wait(2)
followers  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
print("followers len is {}".format(len(followers)))

i = 0
for follower in followers:
    i = i + 1
    try:
        driver.implicitly_wait(0.5)
        follow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, 'html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button".format(i)'))
        )
    # follower.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button".format(i))
        r = follower.text
        r = r.split()
        rl = (r[-1])
        print (rl)
        if rl == "Follow":
            print(r[0])
            follow.click()
            driver.implicitly_wait(0.5)
    except Exception as e:
        print(e)
        continue
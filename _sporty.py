from itertools import permutations
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
bc = []
booking_codes = []
todays_codes = []
booking_code = ''
example = input('Input Todays Example: \n').strip()
todays_trend = example[0:5].upper()
last3 =  example[5:8].upper()
range = input('Range: \n')
indexer = int(int(range)/2)
possible_replacements = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def code_gen():
    for y in list(permutations(possible_replacements, 3)):
        rest = ("".join(y))
        if rest.isnumeric():
            continue
        else:
            bc.append(rest)
            print(rest)
    for i in bc:
        if i == last3:
            index_of_last3 = bc.index(i)
            print(index_of_last3)
    print('\n ************************************************************************* \n')

    startcode_index = index_of_last3 - indexer
    if startcode_index < 0:
        s_remaining = abs(startcode_index)
        startcode_index = 0

    endcode_index = index_of_last3 + indexer
    if endcode_index > len(bc):
        e_remaining = abs(endcode_index)
        endcode_index = len(bc)

    if startcode_index == 0 and s_remaining > 0:
        endcode_index = endcode_index + s_remaining

    if endcode_index == len(bc) and e_remaining > 0:
        startcode_index = startcode_index - e_remaining

    for i in bc:
        if bc.index(i) >= startcode_index and bc.index(i) <= endcode_index:
            if bc.index(i) != index_of_last3:
                print(i)
                booking_codes.append(todays_trend+i)
    print("\n")            
    print(len(booking_codes))
    print('\n @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \n')
    print(booking_codes)

    with open("sporty_generated_booking_codes.txt", "w") as output:
        for item in booking_codes:
            output.write('%s\n' % item)

def spammer_bot():
    booking_code = ''

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.sportybet.com")

    for bc in booking_codes:
        booking_code = bc

        try:
            inputfield =  WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#j_betslip > div.m-betslips > div.m-betslip-search > div > div.m-input-wrapper > span > input'))
            )
            inputfield.clear()
            inputfield.send_keys(booking_code)
            driver.implicitly_wait(0.5)
            loadbutton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="j_betslip"]/div[2]/div[1]/div/button'))
            )
            loadbutton.click()
        except:
            try:
                removeall_btn = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#j_betslip > div.m-betslips > div.m-opertaion > div > div > div.m-table-cell.m-align--right > span'))
                        )
                removeall_btn.click()
                inputfield =  WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#j_betslip > div.m-betslips > div.m-betslip-search > div > div.m-input-wrapper > span > input'))
                )
                inputfield.clear()
                inputfield.send_keys(booking_code)
                driver.implicitly_wait(0.5)
                loadbutton = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="j_betslip"]/div[2]/div[1]/div/button'))
                )
                loadbutton.click()
            except:
                clearbtn = driver.find_element_by_xpath('//*[@id="j_betslip"]/div[2]/div[1]/div/div[2]/span/i')
                clearbtn.click()
                inputfield =  WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#j_betslip > div.m-betslips > div.m-betslip-search > div > div.m-input-wrapper > span > input'))
                )
                inputfield.clear()
                inputfield.send_keys(booking_code)
                driver.implicitly_wait(0.5)
                loadbutton = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="j_betslip"]/div[2]/div[1]/div/button'))
                )
                loadbutton.click()

        try:
            betslip = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.ID, 'j_betslip')))
            
            try:
                driver.implicitly_wait(1)
                if len(betslip) > 0:
                    markets = driver.find_elements_by_class_name('m-item-market')
                    for market in markets:
                        if market.text != 'Correct Score':
                            continue
                        if booking_code not in todays_codes:
                            todays_codes.append(booking_code)
                            print(booking_code)
                    driver.find_element_by_xpath('//*[@id="j_betslip"]/div[2]/div[3]/div/div[2]/div[1]/div[1]/i[2]').click()
                else:
                    clearbtn = driver.find_element_by_xpath('//*[@id="j_betslip"]/div[2]/div[1]/div/div[2]/span/i')
                    clearbtn.click()
                    continue

            except:
                try:
                    clearbtn = driver.find_element_by_xpath('//*[@id="j_betslip"]/div[2]/div[1]/div/div[2]/span/i')
                    clearbtn.click()
                    continue
                except:
                    removeall_btn = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#j_betslip > div.m-betslips > div.m-opertaion > div > div > div.m-table-cell.m-align--right > span'))
                        )
                    removeall_btn.click()
                    continue
        except:
            clearbtn = driver.find_element_by_xpath('//*[@id="j_betslip"]/div[2]/div[1]/div/div[2]/span/i')
            clearbtn.click()
            continue

    print(todays_codes)
    driver.quit()

    with open("fixed_odds", "w") as output:
        for item in todays_codes:
            output.write('%s\n' % item)

def send_email():
    if len(todays_codes) > 0:
        aaliyah_email = 'mybookingcodehunter@gmail.com'
        password = 'quiteincorrect'
        reciever = 'upmylevelby1@gmail.com'
        message = 'SPORTY BET \n'
        for odd in todays_codes:
            message = message + odd + '\n'
        print (message)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(aaliyah_email, password)
        server.sendmail(aaliyah_email, reciever, message)
        print('\n ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ \n EMAIL SENT!!!')
        
code_gen()
spammer_bot()   
send_email()
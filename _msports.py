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
example = input('Input Todays Example: \n').strip()
todays_trend = example[0:4].upper()
last3 =  example[4:7].upper()
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

    with open("msports_generated_booking_codes.txt", "w") as output:
        for item in booking_codes:
            output.write('%s\n' % item)

def spammer_bot():
    booking_code = ''
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.msport.com/gh")

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.dialog--wrap.dialog-push-ad > div.dialog.dialog--vnode > div > div > a.m-pop-close-btn > svg'))
    )
    driver.implicitly_wait(0.5)
    element.click()

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-betslip-ball'))
    )
    element.click()
    driver.implicitly_wait(0.5)

    for b_c in booking_codes:
        booking_code = b_c
        inputfield = driver.find_element_by_css_selector('body > div.m-layout.m-home > main > div.m-betslip > div.m-booking-code-wrap > div > div.m-booking-code--main > form > div.m-input-container > div > div > input')
        inputfield.clear()
        inputfield.send_keys(booking_code)
        driver.implicitly_wait(0.2)
        loadbtn = driver.find_element_by_css_selector('body > div.m-layout.m-home > main > div.m-betslip > div.m-booking-code-wrap > div > div.m-booking-code--main > form > button')
        loadbtn.click()
        

        try:
            errorMsg = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-booking-code-wrap > div > div.m-booking-code--main > form > div.m-input-container > p'))
            )

            if errorMsg:
                clear_btn = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-booking-code-wrap > div > div.m-booking-code--main > form > div.m-input-container > div > div > span > div > svg'))
                )
                clear_btn.click()
                continue

        except:
            
            try:
                fixed = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-summary-container > div > div.m-list-wrap'))
                )
                if fixed:
                    todays_codes.append(booking_code)
                    closeFixed = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-summary-container > div > div.m-list-wrap > div > div.m-bet-selection--wrap > div.selection--inner > div.m-bet-selection--close > div'))
                    )
                    closeFixed.click()

                    entbookc = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-betslip-ball'))
                    )
                    entbookc.click()

                    clear_btn = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-booking-code-wrap > div > div.m-booking-code--main > form > div.m-input-container > div > div > span > div > svg'))
                    )
                    clear_btn.click()
                    continue
            except:  
                try:   
                    betslip_container = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-summary-container > div > div.m-summary-info--main > div.m-flex-left > div.m-title'))
                    )
                    betslip_container.click()

                    removeall_btn = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-main-betslip > div.m-main-betslip--top > div.m-betslip-setting > div.m-betslip-setting-main.flex.align-items-center.justify-content-between > div.flex.align-items-center.justify-content-end > div:nth-child(1) > svg'))
                    )
                    removeall_btn.click()

                    confirm_btn = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.dialog--wrap > div.dialog > div > div.dialog--footer.horizontal > a.btn.btn--ok'))
                    )
                    confirm_btn.click()

                    entbookc = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-betslip-ball'))
                    )
                    entbookc.click()

                    clear_btn = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-booking-code-wrap > div > div.m-booking-code--main > form > div.m-input-container > div > div > span > div > svg'))
                    )
                    clear_btn.click()
                    continue
                except:
                    clear_btn = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.m-layout.m-home > main > div.m-betslip > div.m-booking-code-wrap > div > div.m-booking-code--main > form > div.m-input-container > div > div > span > div > svg'))
                    )
                    clear_btn.click()

    print(todays_codes)
    driver.quit()

def send_email():
    if len(todays_codes) > 0:
        aaliyah_email = 'mybookingcodehunter@gmail.com'
        password = 'quiteincorrect'
        reciever = 'upmylevelby1@gmail.com'
        message = 'MSPORTS \n'
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
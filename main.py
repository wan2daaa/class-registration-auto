from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def sugang():

    # id, password 자기 것으로 변경
    URL = "http://kupis.kku.ac.kr/wsugang/"
    id = ''
    password = ''



    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")
    driver = webdriver.Chrome('chrome/chromedriver')
    driver.get(url=URL)

    driver.implicitly_wait(2)

    driver.switch_to.frame("Main")

    # id 입력
    id_element = driver.find_element(By.XPATH , '//*[@id="id"]')
    id_element.send_keys(id)

    # password  입력
    password_element = driver.find_element(By.XPATH, '//*[@id="pwd"]')
    password_element.send_keys(password)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.XPATH, '//*[@id="form"]/button')
    login_button.click()

    # 로딩 대기
    driver.implicitly_wait(5)

    driver.switch_to.frame("contentFrame")
    driver.switch_to.frame("topFrame")


    # #수강신청할 떄 사용 9시 59분 53초 쯤 실행
    # while(True):
    #     time.sleep(0.3)
    #     clock = driver.find_element(By.XPATH, '//*[@id="dpTime"]/span')
    #     print(clock.text)
    #     if(clock.text == "00"):
    #         break


    click = driver.find_element(By.XPATH, '//*[@id="cssmenu"]/ul/li[3]/a' )
    click.click()

    driver.implicitly_wait(5)

    driver.switch_to.parent_frame()
    driver.switch_to.frame("mainFrame")

    driver.implicitly_wait(5)

    while(True):

        for x in range(1, 2):
            self_xpath = '//*[@id="'+ str(x) +'"]'
            try:
                print(x)
                row = driver.find_element(By.XPATH, self_xpath)

                td1 = row.find_elements(By.TAG_NAME, "td")[13]
                # print(td1.text)
                td2 = row.find_elements(By.TAG_NAME, "td")[14]
                # print(td2.text)
                td3 = row.find_elements(By.TAG_NAME, "td")[16]
                if (td1.text != td2.text):
                    td3.click()
                    driver.implicitly_wait(3)
                    driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/button[1]").click()
                    driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/button").click()
                    print("성공")

                else:
                    print(x + "자리꽉")

            except:
                continue

        driver.switch_to.parent_frame()
        driver.switch_to.frame("topFrame")

        click.click()

        time.sleep(0.3)
        print("새로고침")
        driver.implicitly_wait(5)

        driver.switch_to.parent_frame()
        driver.switch_to.frame("mainFrame")





sugang()


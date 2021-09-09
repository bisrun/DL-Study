from selenium import webdriver
#from selenium.webdriver import ChromeOptions
#from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
#driver.implicitly_wait(10) #

driver.get("https://ngwx.bizmeka.com/LoginN.aspx?compid=mappers")

elem_login=driver.find_element_by_id("TextUserID")
elem_login.clear()
elem_login.send_keys("flywhale")
elem_login = driver.find_element_by_id("TextPassword")
elem_login.send_keys("ms65i18i1*")
xpath_login="""//*[@id="LoginButton"]"""


driver.find_element_by_xpath(xpath_login).click()


try:
    elem_mainFrame=driver.find_element_by_xpath("""//*[@id="mainFrame"]""")
    driver.switch_to.frame(elem_mainFrame)
    fm_myframe = driver.find_element_by_xpath("""//*[@id="subtdc32c"]/iframe""")
    driver.switch_to.frame(fm_myframe)
    driver.find_element_by_xpath("""//*[@id="disIN"]""").click()
    #elem_gotowork_button = driver.find_element_by_id("disIN")
    #elem_gotowork_button.send_keys(Keys.ENTER)
    #
    #
    #elem_gotowork_button.
except Exception as e:
    print("exception ", e)
    pass

try:
    result  = driver.switch_to_alert()
    #alert message 확인
    print(result.text)

    #alert 창 확인
    result.accept()
    #alert 창 끄기
    #result.dismiss()
except Exception as e:
    print("exception ", e)

driver.switch_to.default_content()#처음 상태로 되돌아옴
print("finish")




xpath_gooffwork_button="""//*[@id="disOUT"]"""


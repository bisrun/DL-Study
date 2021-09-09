# -*- coding: utf-8 -*-
from selenium import webdriver

#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from nvconfig import nvconfig
from nvlogger import Logger
import sys
import argparse
from datetime import datetime

#실행명령
#C:\anaconda3\envs\env05\python E:\project2\study\DL-Study\getoffwork\checkwork.py
#  --target=IN --config="E:/project2/study/DL-Study/getoffwork/nvconfig.ini"


class checkwork:
    def __init__(self):
        logManager = Logger.instance()
        self._logger = logManager.getLogger()
        self._logger.info("---c1---")
        self.config = nvconfig.instance()
        self._logger.info("---c2---")
        try:
            self._logger.info("---c3---")
            options = webdriver.ChromeOptions()
            self._logger.info("---c4---")
            options.add_argument('headless')
            options.add_argument('window-size=1920x1080')
            options.add_argument("disable-gpu")

            self.driver = webdriver.Chrome(self.config._DriverPath, chrome_options=options )
            self._logger.info("---c7---")
        except Exception as e:
            self._logger.error("init exception ", e)
            exit()
    #step 1
    def login(self):
        self._logger.info("try to login")
        #driver.implicitly_wait(10) #
        self._logger.info("--2--")
        try:
            self.driver.get(self.config._initUrl)
            self.driver.implicitly_wait(3)
            elem_login=self.driver.find_element_by_id("TextUserID")
            elem_login.clear()
            elem_login.send_keys(self.config._loginId)
            self._logger.info("--3--")
            elem_login = self.driver.find_element_by_id("TextPassword")
            elem_login.send_keys(self.config._loginPwd)

            self._logger.info("--4--")
            #button click
            self.driver.find_element_by_xpath("""//*[@id="LoginButton"]""").click()
            self._logger.info("--5--")
            self.driver.implicitly_wait(3)
            self._logger.info("--6--")
        except Exception as e:
            self._logger.error("login exception ", e)
            exit()
    #step 2
    def targetClick(self, target):
        try:
            #이 페이지는 여러 프레임으로 구성되어있다. 원하는 element를 찾기위해, frame을 찾아간다.
            elem_mainFrame=self.driver.find_element_by_xpath("""//*[@id="mainFrame"]""")
            self.driver.switch_to.frame(elem_mainFrame)

            fm_myframe = self.driver.find_element_by_xpath("""//*[@id="subtdc32c"]/iframe""")
            self.driver.switch_to.frame(fm_myframe)

            self._logger.info("target :%s", target )
            #출석 버튼
            if "IN" == target.upper():
                self.driver.find_element_by_xpath("""//*[@id="disIN"]""").click()
            elif "OUT" == target.upper():
                self.driver.find_element_by_xpath("""//*[@id="disOUT"]""").click()
            else:
                self._logger.error("invalid target :", target )

        except Exception as e:
            self._logger.error("targetClick exception ", e)
            pass

        #만약 popup 창이 있다면 닫는다.
        try:
            result  = Alert(self.driver)
            #alert message 확인
            self._logger.info(result.text)
            #alert 창 확인
            result.accept()
        except Exception as e:
            self._logger.error("targetClick exception(close popup) ", e)
            pass

    def close(self):
        self.driver.switch_to.default_content() #처음 상태로 되돌아옴
        self.driver.close()
        self.driver.quit()
        self._logger.info("finish")


def run(target):
    try :

        cm = checkwork()
        cm.login()
        cm.targetClick(target)
        cm.close()


    except Exception as e:
        print("exception ", e)


if __name__ == '__main__':


    argParser = argparse.ArgumentParser()
    argParser.add_argument('--target', required=True, help='출근이니 퇴근이니? in/out')
    argParser.add_argument('--config', required=False, help='config file path')
    argret = argParser.parse_args()

    try :
        args = argParser.parse_args()

        cc = nvconfig.instance()
        cc.setInit(args.config)
        ret = cc.load_file()
        if ret < 0 :
            exit()

        logManager = Logger.instance()
        logManager.setLogger(cc._logFilePath)
        logger = logManager.getLogger()
        logger.info("-------------start--------------")
        logger.info("target: %s", args.target)

        if args.target.upper() == "OUT" :
            now = datetime.now().time()
            if now.hour < 18 or now.minute < 3  :
                logger.info("18:03전에 호출됨. 종료함")
                exit()
        logger.info("--1--")
        run(args.target)
    except argparse.ArgumentError:
        print('Catching an argumentError')

    sys.exit()



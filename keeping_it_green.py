#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class KeepingGreenTestCase(unittest.TestCase):
    def setUp(self):

        # Headless
        options = webdriver.ChromeOptions()
        options.headless = True

        # PATH to chromedriver
        self.driver = webdriver.Chrome("CHROMEDRIVER_PATH", options = options)

        # Wait time
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_keepinggreen_test_case(self):
        driver = self.driver
        driver.get("https://github.com/login")

        # YOUR_USERNAME in login_field
        driver.find_element_by_id("login_field").send_keys("YOUR_USERNAME")
        driver.find_element_by_id("password").clear()

        # YOUR_PASSWORD in login_field
        driver.find_element_by_id("password").send_keys("YOUR_PASSWORD")
        driver.find_element_by_id("login_field").click()
        driver.find_element_by_name("commit").click()

        # Link to your dummy file inside your dummy repo
        driver.get("LINK_TO_DUMMY_FILE")
        driver.find_element_by_css_selector("svg.octicon.octicon-trashcan").click()
        driver.find_element_by_id("submit-file").click()

        # Name of your dummy file - change the following
        driver.get("https://github.com/YOUR_USERNAME/DUMMY-REPO-NAME/new/master")
        driver.find_element_by_name("filename").send_keys("NAME_DUMMY_FILE")
        driver.find_element_by_id("submit-file").click()
        driver.close()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

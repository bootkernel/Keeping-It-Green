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

""" 
******************************************************************************************************************************************
Keeping It Green is a super simple python script that uses Selenium to help you keep committed to GitHub even when you're sleeping.
Copyright (C) 2019  Subhajeet Mukherjee

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

******************************************************************************************************************************************
"""


class KeepingGreenTestCase(unittest.TestCase):
    def setUp(self):

        # PATH to chromedriver
        self.driver = webdriver.Chrome("CHROMEDRIVER_PATH")

        # Change wait_time
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

        # Link to your dummy project repo
        driver.get("DUMMY_PROJECT_REPO_URL")
        
        driver.find_element_by_id("9f27410725ab8cc8854a2769c7a516b8-8b137891791fe96927ad78e64b0aad7bded08bdc").click()
        driver.find_element_by_css_selector("svg.octicon.octicon-trashcan").click()
        driver.find_element_by_id("submit-file").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='New pull request'])[1]/following::button[1]").click()
        driver.find_element_by_name("filename").clear()

        # NAME of your dummy file
        driver.find_element_by_name("filename").send_keys("NAME_DUMMY_FILE")

        driver.find_element_by_id("submit-file").click()
        driver.close()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

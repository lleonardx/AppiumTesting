import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity',
    automationName='UiAutomator2'
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/nine').click()
driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/eight').click()
driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/four').click()
driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/four').click()
driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/six').click()
driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/tree').click()
driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/nine').click()
driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/five').click()
driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/one').click()

time.sleep(2)
driver.quit()
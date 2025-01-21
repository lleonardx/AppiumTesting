import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


def dial_number(driver, number):
    mapping = {
        '0': 'com.samsung.android.dialer:id/zero',
        '1': 'com.samsung.android.dialer:id/one',
        '2': 'com.samsung.android.dialer:id/two',
        '3': 'com.samsung.android.dialer:id/three',
        '4': 'com.samsung.android.dialer:id/four',
        '5': 'com.samsung.android.dialer:id/five',
        '6': 'com.samsung.android.dialer:id/six',
        '7': 'com.samsung.android.dialer:id/seven',
        '8': 'com.samsung.android.dialer:id/eight',
        '9': 'com.samsung.android.dialer:id/nine',
    }

    for digit in number:
        if digit in mapping:
            driver.find_element(AppiumBy.ID, mapping[digit]).click()
        else:
            print(f"Invalid digit: {digit}")


#Appium config
desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity',
    automationName='UiAutomator2'
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

#Number to Dial
number_to_dial = "984463951"

dial_number(driver, number_to_dial)

driver.find_element(AppiumBy.ID, 'com.samsung.android.dialer:id/dialButtonImage').click()

time.sleep(2)
driver.quit()

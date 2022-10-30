from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

desired_cap = {
    # Set your access credentials
    "browserstack.user": "gemohin_E7lXDx",
    "browserstack.key": "youykhRmvMxn4EH8vc3M",

    # Set URL of the application under test
    "app": "bs://40932f698ddd672d9498fffc2a231ba9d7e8d186",
    "otherApps": ["bs://6631a045a17783ce11fc0276d965da00b0a6a29d"],
    # image injection
    "browserstack.enableCameraImageInjection": "true",

    # Specify device and os_version for testing
    "device": "Google Pixel 3",
    "os_version": "9.0",

    # Set other BrowserStack capabilities
    "project": "First Python project",
    "build": "browserstack-build-1",
    "name": "first_test"

}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)


@pytest.mark.run(order=1)
def testAdda():
    # Test case for the BrowserStack sample Android app.
    # If you have uploaded your app, update the test case here.
    skip_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.adda:id/tv_skip"))
    )
    skip_button.click()
    # Click on switch email
    switch_Email = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.adda:id/tv_switch_email_mobile"))
    )
    switch_Email.click()
    # Passing Email Id
    Send_email = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.adda:id/et_email_id"))
    )
    Send_email.send_keys("muaauto@gma.com")
    # send password
    Send_password = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.adda:id/et_password"))
    )
    Send_password.send_keys("adda1234")
    # click on login
    click_login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.adda:id/tv_login"))
    )
    click_login.click()
    # Invoke driver.quit() after the test is done to indicate that the test is completed.


@pytest.mark.run(order=2)
def testswitchGate():
    time.sleep(5)
    driver.activate_app("com.threefiveeight.addagatekeeper")
    click_widget = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "android:id/switch_widget"))
    )
    click_widget.click()
    driver.back()
    for x in range(0, 5):
        click_Allow = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button"))
        )
        click_Allow.click()
    gk_email = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/etLoginUsername"))
    )
    gk_email.send_keys("muaautogk@gmai.com")
    gk_password = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/etLoginPassword"))
    )
    gk_password.send_keys("adda1234")
    gk_login = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/btnLoginButton"))
    )
    gk_login.click()
    gk_proceed = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/btn_proceed"))
    )
    gk_proceed.click()


@pytest.mark.run(order=3)
def testAddaSingleUnit():
    gk_enterunit = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/fcv_flats"))
    )
    gk_enterunit.click()
    driver.press_keycode(13)
    time.sleep(2)
    driver.press_keycode(66)
    gk_clickNext = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/b_next"))
    )
    gk_clickNext.click()
    user_mob = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/et_visitor_mobile"))
    )
    user_mob.send_keys("9846479950")
    driver.hide_keyboard()
    gk_enterunit = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/fcv_flats"))
    )
    gk_enterunit.click()
    driver.hide_keyboard()
    visitor_verification = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/b_check_in_visitor"))
    )
    visitor_verification.click()
    time.sleep(3)
    driver.open_notifications()
    visitor_allow = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@content-desc=\"Allow\"]"))
    )
    visitor_allow.click()
    driver.back()


@pytest.mark.run(order=4)
def testGateSingleEntry():
    time.sleep(2)
    actions = TouchAction(driver)
    actions.long_press(None, 480, 985).move_to(None, 465, 1649).release().perform()
    gk_checkin_tab = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@text='CHECK IN']"))
    )
    gk_checkin_tab.click()
    time.sleep(3)
    checkOut = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.LinearLayout/android.widget.TextView"
    gk_checkout_tab = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, checkOut))
    )
    gk_checkout_tab.click()
    time.sleep(3)
    actions = TouchAction(driver)
    actions.long_press(None, 480, 985).move_to(None, 465, 1649).release().perform()
    time.sleep(2)
    gk_checkout = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/btnStaff"))
    )
    gk_checkout.click()
    time.sleep(3)
    gk_checkout_with_out_photo = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/checkout"))
    )
    gk_checkout_with_out_photo.click()
    time.sleep(5)


# @pytest.mark.run(order=5)
# def testStaffCheckIn():
#     time.sleep(10)
#     staff_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.LinearLayout/android.widget.ImageView"
#     click_staff = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, staff_xpath))
#     )
#     click_staff.click()
#     # in_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.Button"
#     staff_checkIn = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/btnStaff"))
#     )
#     time.sleep(5)
#     staff_checkIn.click()
#     temp_check_in = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/tv_check_in"))
#     )
#     temp_check_in.click()
#
#
# @pytest.mark.run(order=6)
# def testStaffCheckOut():
#     staff_out_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.LinearLayout/android.widget.TextView"
#     click_check_out = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, staff_out_xpath))
#     )
#     click_check_out.click()
#     staff_checkOut = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/btnStaff"))
#     )
#     staff_checkOut.click()
#     staff_FinalcheckOut = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "android:id/button1"))
#     )
#     staff_FinalcheckOut.click()
#
#
# @pytest.mark.run(order=7)
# def testdenyuser():
#     home_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"
#     home_page = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, home_xpath))
#     )
#     home_page.click()
#     gk_enterunit = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/fcv_flats"))
#     )
#     gk_enterunit.click()
#     driver.press_keycode(13)
#     time.sleep(2)
#     driver.press_keycode(66)
#     gk_clickNext = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/b_next"))
#     )
#     gk_clickNext.click()
#     user_mob = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/et_visitor_mobile"))
#     )
#     user_mob.send_keys("9846479950")
#     driver.hide_keyboard()
#     visitor_verification = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/b_check_in_visitor"))
#     )
#     visitor_verification.click()
#     time.sleep(3)
#     driver.open_notifications()
#     visitor_allow = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@content-desc=\"Deny\"]"))
#     )
#     visitor_allow.click()
#     driver.back()
#     time.sleep(5)
#     gate_check_out = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@text='DENY']"))
#     )
#     gate_check_out.click()
#     time.sleep(10)
#
# @pytest.mark.run(order=8)
# def testneverloggedin():
#     driver.back()
#     gk_enterunit = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/fcv_flats"))
#     )
#     gk_enterunit.click()
#     driver.press_keycode(9)
#     time.sleep(2)
#     driver.press_keycode(66)
#     gk_clickNext = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/b_next"))
#     )
#     gk_clickNext.click()
#     user_mob = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/et_visitor_mobile"))
#     )
#     user_mob.send_keys("9846479950")
#     driver.hide_keyboard()
#     visitor_verification = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/b_check_in_visitor"))
#     )
#     visitor_verification.click()
#     time.sleep(3)
#     no_answer = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/no_answer_tv"))
#     )
#     no_answer.click()
#     check_in = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/b_check_in_visitor"))
#     )
#     check_in.click()
#     time.sleep(5)
#     check_out_tab = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, "android.widget.TextView[@text='Check Out']"))
#     )
#     check_out_tab.click()
#     staff_checkIn = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/btnStaff"))
#     )
#     time.sleep(5)
#     staff_checkIn.click()
#     temp_check_in = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/tv_check_in"))
#     )
#     temp_check_in.click()
# @pytest.mark.run(order=9)
# def testneverloggedin():
#     driver.back()
#     gk_enterunit = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/fcv_flats"))
#     )
#     gk_enterunit.click()
#     driver.press_keycode(9)
#     time.sleep(2)
#     driver.press_keycode(66)
#     time.sleep(2)
#     driver.press_keycode(13)
#     time.sleep(2)
#     driver.press_keycode(66)
#     gk_clickNext = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/b_next"))
#     )
#     gk_clickNext.click()
#     user_mob = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/et_visitor_mobile"))
#     )
#     user_mob.send_keys("9846479950")
#     driver.hide_keyboard()
#     gk_multi_next = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@text='NEXT']"))
#     )
#     gk_multi_next.click()
#     driver.open_notifications()
#     visitor_allow = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@content-desc=\"Allow\"]"))
#     )
#     visitor_allow.click()
#     driver.back()
#     click_next = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/button_action"))
#     )
#     click_next.click()
#
#     visitor_allow_answer = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/deny_card"))
#     )
#     visitor_allow_answer.click()
#     gk_checkin_tab = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@text='CHECK IN']"))
#     )
#     gk_checkin_tab.click()
#     time.sleep(5)
#     checkOut = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.LinearLayout/android.widget.TextView"
#     gk_checkout_tab = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.XPATH, checkOut))
#     )
#     gk_checkout_tab.click()
#     gk_checkout = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/btnStaff"))
#     )
#     gk_checkout.click()
#     gk_checkout_with_out_photo = WebDriverWait(driver, 30).until(
#         EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/checkout"))
#     )
#     gk_checkout_with_out_photo.click()
#     driver.back()

@pytest.mark.run(order=10)
def testLogoutGate():
    home_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"
    home_page = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, home_xpath))
    )
    home_page.click()
    # nav_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"
    nav_logout = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.threefiveeight.addagatekeeper:id/nav_icon"))
    )
    nav_logout.click()
    logout_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.LinearLayout[8]/android.widget.TextView"
    click_logout = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, logout_xpath))
    )
    click_logout.click()
    click_logout = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, "android:id/button1"))
    )
    click_logout.click()
    driver.quit()
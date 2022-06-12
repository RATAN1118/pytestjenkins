from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def test_setup():
    global driver
    driver = webdriver.Chrome("C:\\Users\\GSC-30966\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()


@pytest.mark.parametrize(
    "username, password",
    [("standard_user", "secret_sauce"), ("locked_out_user", "secret_sauce")]

)
def test_login(test_setup, username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element_by_id("user-name").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login-button").click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_close():
    driver.close()
    driver.quit()
    print("test completed")

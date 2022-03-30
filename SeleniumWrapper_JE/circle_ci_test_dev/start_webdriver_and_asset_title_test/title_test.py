from selenium_wrapper import get_webdriver

firefox_webdriver_wrapper = get_webdriver("edge")

firefox_webdriver = firefox_webdriver_wrapper.webdriver

firefox_webdriver.get("http://www.python.org")

firefox_webdriver.implicitly_wait(1)

assert firefox_webdriver.title == "Welcome to Python.org"

firefox_webdriver_wrapper.close()

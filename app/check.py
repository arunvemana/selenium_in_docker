from time import sleep
import socket
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

sleep(10)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

driver = webdriver.Remote(
    command_executor=f'http://selenium:4444/wd/hub',
    options=webdriver.ChromeOptions()
)

driver.get('http://python.org/')
driver.save_screenshot('screenshot.png')
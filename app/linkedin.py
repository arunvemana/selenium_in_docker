from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credits import EMAIL, PASSWORD,COMPANYNUMBER
import logging

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler("logfile.log")
formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)
sleep(5)
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument('--disable-features=RendererCodeIntegrity')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Remote(
    command_executor=f'http://selenium:4444/wd/hub',
    options=options
)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

sleep(2)
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(EMAIL)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
except Exception as e:
    logger.error(e)
    driver.quit()
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)

driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.ENTER)
sleep(2)
driver.save_screenshot('sucessfully_login_screenshot.png')
driver.execute_script('''document.querySelector('a[data-control-name="pages_admin_module_visitor_analytics_cta"]').click()''')

driver.get(f"https://www.linkedin.com/company/{COMPANYNUMBER}/admin/analytics/followers/")


driver.implicitly_wait(20)
driver.save_screenshot('followers_page_screenshot.png')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "org-view-page-followers-module__modal-button"))
    )
except Exception as e:
    logger.error(e)
    driver.quit()
followers_model = driver.find_element(By.CLASS_NAME,"org-view-page-followers-module__modal-button")
logger.debug(followers_model)
sleep(5)
followers_model.send_keys(Keys.ENTER)
driver.save_screenshot("open followers module.png")
# scroll = driver.find_element(By.CLASS_NAME,"org-view-page-followers-modal__infinite-scroll-container overflow-scroll")
scrollheight_p = 0
while True:
    try:
        scrollheight = driver.execute_script('return document.getElementsByClassName("org-view-page-followers-modal__infinite-scroll-container overflow-scroll")[0].scrollHeight')
        driver.execute_script(f'document.getElementsByClassName("org-view-page-followers-modal__infinite-scroll-container overflow-scroll")[0].scroll(0,{scrollheight})')
        sleep(2)
        if scrollheight_p != scrollheight:
            scrollheight_p = scrollheight
        else:
            sleep(1)
            break
    finally:
        break
driver.save_screenshot("scrolled followers module.png")
table_data = driver.find_elements(By.CLASS_NAME,"org-view-page-followers-modal__table-row")
table_data1 = [element.get_attribute('innerHTML') for element in table_data]
with open('table_data.html','w') as f:
    f.write(str(table_data1))
hrefs = []
for i in table_data:
    links = i.find_elements(By.TAG_NAME,'a')
    hrefs.append(links[0].get_attribute('href'))
print("*"*1000)
print(hrefs)
with open("data.txt",'w') as f:
    for item in hrefs:
        f.write("%s\n" % item)
driver.quit()

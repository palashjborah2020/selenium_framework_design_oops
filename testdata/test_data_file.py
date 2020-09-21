import os
browser = 'chrome'
#url = "https://www.google.co.in"
url = "https://www.goibibo.com/"
search_value = "Selenium"
wait_time = 20


chrome_driver_path = "E:\\driver\\chromedriver.exe"
firefox_driver_path = "E:\\driver\\geckodriver.exe"
edge_driver_path = "E:\\driver\\msedgedriver.exe"

CUR_DIR = os.getcwd()
LOG_DIR = os.path.join(CUR_DIR, 'log')
IMAGE_DIR = os.path.join(CUR_DIR, 'image')
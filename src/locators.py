from selenium.webdriver.common.by import By
from framework_design_oops.testdata.constant import *

XPATH = By.XPATH
NAME = By.NAME
CSS = By.CSS_SELECTOR
ID = By.ID
LINKTEXT = By.LINK_TEXT


GOOGLE_SEARCH_BOX = (NAME, "q")
GOOGLE_SEARCH_BUTTON = (NAME, "btnK")

# Goibibo Go website locators
HOTELS_ICON = (XPATH, "//a[@href='/hotels/']//span[text()='Hotels']")
INDIA_RADIO_LABEL = (XPATH, "(//input[@name='CountryType'])[1]")
HOTEL_LANDMARK = (ID, "downshift-1-input")
HOTE_PAGE_HEADER_ELEMENT = (XPATH, f"//h1[contains(text(), '{HOTEL_PAGE_HEADER}')]")
HOTEL_LOCATION_DROP_DOWN = (ID, "downshift-1-menu")





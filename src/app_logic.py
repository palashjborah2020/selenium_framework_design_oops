from framework_design_oops.browser_actions.browser_actions import BrowserAction
from .locators import *
from datetime import datetime

class AppFunction(BrowserAction):

    def __init__(self, browser, url, wait_time):
        self.url = url
        super().__init__(browser, wait_time)
        self.launch_app()

    def  launch_app(self):
        self.spdriver.get(self.url)

    def close_browser(self):
        self.spdriver.close()

    def search_on_google(self, value):
        self.input_text(GOOGLE_SEARCH_BOX, value)
        self.click_element(GOOGLE_SEARCH_BUTTON)

    def navigate_hotel_page(self):
        self.click_element(HOTELS_ICON)
        self.verify_element_is_visible(HOTE_PAGE_HEADER_ELEMENT)
        cur_time = str(datetime.time(datetime.now()))
        filename = f"{cur_time}_hotels.png"
        self.take_screen_shot(filename)


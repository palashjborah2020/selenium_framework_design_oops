from framework_design_oops.testdata.test_data_file import *
import logging
logger = logging.getLogger(__name__)
import  pytest




@pytest.mark.skip()
def test_search_on_google(setup):
    try:
        logger.info("test cases: test_search_on_google, executed started")
        setup.search_on_google(search_value)
        setup.close_browser()
        logger.info("test cases: test_search_on_google, executed successfully")
    except Exception as e:
        logging.exception(f"test case : test_search_on_google, execution failed :")
        raise(e)


def test_book_hotel(setup):
    logger.info("test cases: test_book_hotel, executed started")
    setup.navigate_hotel_page()

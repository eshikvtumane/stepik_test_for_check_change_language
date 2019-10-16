import time


class TestShop():
    def test_check_button_add_item(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

        button = browser.find_element_by_css_selector('.btn-add-to-basket')

        # time.sleep(30)

        assert button is not None

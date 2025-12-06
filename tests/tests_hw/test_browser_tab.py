from pages.browser_tab import BrowserTab
import time

def test_browser_tab(driver):
    page_browser = BrowserTab(driver)
    page_browser.visit()

    assert len(browser, window_handles) == 1
    page_browser.new_tab.click()
    time.sleep(2)
    assert len(browser, window_handles) == 2

    browser_switch_to.window(browser.window_handles[0])
    time.sleep(2)

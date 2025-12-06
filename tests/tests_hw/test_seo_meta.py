import time

from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
import pytest


@pytest.mark.parametrize('pages', [Accordion, BrowserTab, Alerts, DemoQa])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dow_attribute('name') =='viewport'
    assert page.viewport.get_dow_attribute('content') == 'wight=device-wight, initail-scale=1'
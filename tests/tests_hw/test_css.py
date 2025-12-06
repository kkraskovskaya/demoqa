from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box = TextBox(browser)

    text_box.visit()

    assert text_box.submit.check_css('color' , 'rgba(255, 255, 255, 255, 1)')
from YandexPages import SearchHelper
from urllib.parse import urlparse


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    element_search = yandex_main_page.get_search_field()
    assert element_search is not None

    yandex_main_page.enter_word("тензор")
    element_suggest = yandex_main_page.get_suggest()
    assert element_suggest is not None

    yandex_main_page.click_on_the_enter()
    links = yandex_main_page.get_links()
    for i in range(5):
        assert "tensor.ru" in urlparse(links[i]).netloc


def test_yandex_pictures(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    element_pictures = yandex_main_page.get_pictures()
    assert element_pictures is not None

    yandex_main_page.click_on_the_picture()
    yandex_main_page.go_to_second_window()
    current_url = yandex_main_page.get_url()
    assert 'https://yandex.ru/images/' in current_url

    name_of_the_first_category = yandex_main_page.get_name_of_the_first_category()
    yandex_main_page.click_on_the_first_category()
    assert name_of_the_first_category == yandex_main_page.get_text_from_search_field()

    yandex_main_page.click_on_the_first_picture()
    image_src = yandex_main_page.get_image_src()
    yandex_main_page.click_on_the_next_button()
    yandex_main_page.click_on_the_before_button()
    assert image_src == yandex_main_page.get_image_src()

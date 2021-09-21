from selenium.webdriver.common.keys import Keys
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_FIELD_IN_PICTURES = (By.NAME, "text")
    LOCATOR_YANDEX_IMAGES = (By.CSS_SELECTOR, "[data-id='images']")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup_visible")  # mini-suggest__popup_visible
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CLASS_NAME, "service__name")
    LOCATOR_YANDEX_LINKS = (By.CLASS_NAME, "organic__url")
    LOCATOR_YANDEX_FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    LOCATOR_YANDEX_IMAGE = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_YANDEX_NEXT_BUTTON = (By.CLASS_NAME, "CircleButton_type_next")
    LOCATOR_YANDEX_BEFORE_BUTTON = (By.CLASS_NAME, "CircleButton_type_prev")
    LOCATOR_YANDEX_FIRST_PICTURE = (By.CLASS_NAME, "serp-item_pos_0")


class SearchHelper(BasePage):
    def get_search_field(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    def get_suggest(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST)

    def get_pictures(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES)

    def get_image_src(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGE).get_attribute("src")

    def get_first_category(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY)

    def enter_word(self, word):
        search_field = self.get_search_field()
        search_field.click()
        search_field.send_keys(word)
        return

    def click_on_the_enter(self):
        search_field = self.get_search_field()
        search_field.send_keys(Keys.RETURN)
        return

    def click_on_the_picture(self):
        pictures = self.get_pictures()
        pictures.click()
        return

    def get_links(self):
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_LINKS, time=2)
        links = [x.get_attribute("href") for x in all_list]
        return links

    def click_on_the_first_category(self):
        category = self.get_first_category()
        category.click()
        return

    def get_name_of_the_first_category(self):
        category = self.get_first_category()
        return category.get_attribute("data-grid-text")

    def get_text_from_search_field(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD_IN_PICTURES)
        return search_field.get_attribute("value")

    def click_on_the_next_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_NEXT_BUTTON).click()

    def click_on_the_before_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_BEFORE_BUTTON).click()

    def click_on_the_first_picture(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_PICTURE).click()

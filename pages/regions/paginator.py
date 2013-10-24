#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class Paginator(Page):

    # Page numbering
    _page_number_locator = (By.CSS_SELECTOR, '.current > strong')
    _total_page_number_locator = (By.CSS_SELECTOR, '.pagination ol .last > a')
    _current_page_locator = (By.CSS_SELECTOR, '.page-status')

    # Page navigation
    _prev_locator = (By.CSS_SELECTOR, '.prev > a')
    _next_locator = (By.CSS_SELECTOR, '.next > a')
    _middle_page_locator = (By.CSS_SELECTOR, '.pagination > ol > li:nth-child(6) > a')

    @property
    def page_number(self):
        return int(self.selenium.find_element(*self._page_number_locator).text)

    @property
    def total_page_number(self):
        return int(self.selenium.find_element(*self._total_page_number_locator).text)

    @property
    def current_page_number(self):
        text = self.selenium.find_element(*self._current_page_locator).text
        return int(text.split()[1])

    @property
    def page_x_of_y_message(self):
        return self.selenium.find_element(*self._current_page_locator).text

    def click_prev_page(self):
        self.selenium.find_element(*self._prev_locator).click()

    @property
    def is_prev_page_visible(self):
        return self.is_element_visible(*self._prev_locator)

    @property
    def is_next_page_visible(self):
        return self.is_element_visible(*self._next_locator)

    def click_next_page(self):
        self.selenium.find_element(*self._next_locator).click()

    def click_last_page(self):
        self.selenium.find_element(*self._total_page_number_locator).click()

    def click_middle_page(self):
        self.selenium.find_element(*self._middle_page_locator).click()

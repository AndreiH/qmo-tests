#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class TagResultsPage(BasePage):

    _page_title = u'Posts tagged'

    def tag_results_page(self):
        self.selenium.get(self.testsetup.base_url + '/tag/a11y/')
        self.is_the_current_page

    @property
    def is_page_title_correct(self):
        return self.selenium.get_title() == self._page_title

    @property
    def results(self):
        return self.selenium.find_elements(By.CSS_SELECTOR, "#content-main > article")

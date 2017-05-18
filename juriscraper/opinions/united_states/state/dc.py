"""Scraper for the D.C. Court of Appeals
CourtID: dc
Court Short Name: D.C.
Author: V. David Zvenyach
Date created:2014-02-21
"""

from juriscraper.OpinionSite import OpinionSite
from juriscraper.lib.string_utils import convert_date_string


class Site(OpinionSite):
    def __init__(self, *args, **kwargs):
        super(Site, self).__init__(*args, **kwargs)
        self.court_id = self.__module__
        self.url = 'http://www.dccourts.gov/internet/opinionlocator.jsf'
        self.base_path = '//table//tr[not(contains(td[2]/span/text(), "NO OPINIONS"))]'

    def _get_download_urls(self):
        path = '%s/td[1]/a/@href' % self.base_path
        return [href for href in self.html.xpath(path)]

    def _get_case_names(self):
        path = '%s/td[2]' % self.base_path
        return [cell.text_content() for cell in self.html.xpath(path)]

    def _get_case_dates(self):
        path = '%s/td[3]' % self.base_path
        return [convert_date_string(cell.text_content()) for cell in self.html.xpath(path)]

    def _get_precedential_statuses(self):
        return ["Published"] * len(self.case_names)

    def _get_docket_numbers(self):
        path = '%s/td[1]/a' % self.base_path
        return [cell.text_content() for cell in self.html.xpath(path)]

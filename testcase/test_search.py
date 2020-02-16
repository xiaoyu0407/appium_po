from page.xueqiu_page import XueqiuPage

import pytest
class TestSearch:
    def setup_class(self):
        self.xueqiu = XueqiuPage()

    def test_search_us(self):
        assert self.xueqiu.goto_search().search("alibaba").select(0).get_price("BABA") >170

    def test_search_us_other   (self):
        assert "阿里" in self.xueqiu.goto_search().search("alibaba").select(-1).get_name()
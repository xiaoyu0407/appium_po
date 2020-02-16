class TestAds:
    def setup(self):
        self.xueqiu = XueqiuPage()

    def test_ads(self):
        assert self.xueqiu.get_ads() == True

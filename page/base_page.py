class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self):
        #todo: 处理弹框 异常处理 动态浮动的元素的处理
        pass
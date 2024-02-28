from selenium import webdriver
from selenium.webdriver.common.by import By

class BrowserAdapter:
    @staticmethod
    def generate():
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless=new")

        return {'adapter': webdriver.Chrome(options=opts), 'by': By}
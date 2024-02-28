class Retriever:
    def __init__(self, browser, xpath):
        self.browser = browser
        self.xpath = xpath

    def goTo(self, url):
        self.browser.get(url)

    def findElement(self, elementXPath):
        tempElements = self.browser.find_elements(by = self.xpath, value = elementXPath)

        if len(tempElements) < 1:
            return False
        return tempElements[0]

    def writeInElement(self, element, text):
        element.send_keys(text)

    def clickInElement(self, element):
        element.click()

    def close(self):
        self.browser.close()
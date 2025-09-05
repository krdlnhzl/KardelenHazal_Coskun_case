from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://useinsider.com/"
    COMPANY_MENU = (By.XPATH, "//a[contains(text(), 'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[contains(text(), 'Careers')]")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def is_opened(self):
        return "Insider" in self.driver.title

    def go_to_careers(self):
        self.driver.find_element(*self.COMPANY_MENU).click()
        self.driver.find_element(*self.CAREERS_LINK).click()

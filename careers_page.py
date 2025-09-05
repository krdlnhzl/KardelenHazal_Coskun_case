from selenium.webdriver.common.by import By

class CareersPage:
    LOCATIONS_BLOCK = (By.ID, "career-our-location")
    TEAMS_BLOCK = (By.ID, "career-find-our-calling")
    LIFE_BLOCK = (By.ID, "career-life-at-insider")

    def __init__(self, driver):
        self.driver = driver

    def is_locations_block_visible(self):
        return self.driver.find_element(*self.LOCATIONS_BLOCK).is_displayed()

    def is_teams_block_visible(self):
        return self.driver.find_element(*self.TEAMS_BLOCK).is_displayed()

    def is_life_block_visible(self):
        return self.driver.find_element(*self.LIFE_BLOCK).is_displayed()

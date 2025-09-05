from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QAJobsPage:
    SEE_ALL_QA_JOBS = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    LOCATION_FILTER = (By.XPATH, "//select[@id='select2-filter-by-location-container']")
    DEPARTMENT_FILTER = (By.XPATH, "//select[@id='select2-filter-by-department-container']")
    JOB_LIST = (By.CSS_SELECTOR, "div.position-list-item")
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[contains(text(), 'View Role')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://useinsider.com/careers/quality-assurance/")

    def click_see_all_jobs(self):
        self.driver.find_element(*self.SEE_ALL_QA_JOBS).click()

    def filter_jobs(self, location="Istanbul, Turkey", department="Quality Assurance"):
        # Location
        location_dropdown = self.wait.until(EC.element_to_be_clickable(self.LOCATION_FILTER))
        location_dropdown.click()
        self.driver.find_element(By.XPATH, f"//li[contains(text(), '{location}')]").click()

        # Department
        department_dropdown = self.wait.until(EC.element_to_be_clickable(self.DEPARTMENT_FILTER))
        department_dropdown.click()
        self.driver.find_element(By.XPATH, f"//li[contains(text(), '{department}')]").click()

    def get_job_elements(self):
        return self.driver.find_elements(*self.JOB_LIST)

    def click_view_role(self):
        self.driver.find_element(*self.VIEW_ROLE_BUTTON).click()

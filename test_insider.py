import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage

def test_insider_case(driver):
    # Homepage kontrolü
    home = HomePage(driver)
    home.open()
    assert home.is_opened(), "HOMEPAGE AÇILMADI 🫥"

    # Careers sayfası
    home.go_to_careers()
    careers = CareersPage(driver)
    assert careers.is_locations_block_visible(), "Locations görünmüyor 🫥"
    assert careers.is_teams_block_visible(), "Teams görünmüyor 🫥"
    assert careers.is_life_block_visible(), "Life at Insider görünmüyor 🫥"

    # Step 3: QA Jobs 
    qa_page = QAJobsPage(driver)
    qa_page.open()
    qa_page.click_see_all_jobs()
    qa_page.filter_jobs()

    jobs = qa_page.get_job_elements()
    assert len(jobs) > 0, "QA job listesi boş 🫥"
    
    for job in jobs:
        assert "Quality Assurance" in job.text, f"Job filtresi yanlış: {job.text}"
        assert "Istanbul, Turkey" in job.text, f"Lokasyon hatalı: {job.text}"

    qa_page.click_view_role()
    assert "lever.co" in driver.current_url, "Lever sayfasına yönlenmedi 🫥"

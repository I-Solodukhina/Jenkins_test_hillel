import pytest
import allure
from playwright.sync_api import sync_playwright
from registration import RegistrationPage


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@allure.step("Navigate to registration page")
def navigate_to_registration_page(page):
    page.goto('https://guest:welcome2qauto@qauto2.forstudy.space/')
    page.wait_for_load_state('networkidle')
    page.locator(".hero-descriptor_btn.btn.btn-primary").click()


@pytest.fixture
def wd(page):
    wd = RegistrationPage(page)
    navigate_to_registration_page(page)
    return wd


@pytest.fixture
def fill_registration_form(page):
    @allure.step("Fill registration form with data: {first_name}, {last_name}, {email}, ****")
    def _fill_form(first_name, last_name, email, password):
        navigate_to_registration_page(page)

        registration_page = RegistrationPage(page)

        with allure.step("Enter first name"):
            registration_page.get_first_name_input().fill(first_name)
        with allure.step("Enter last name"):
            registration_page.get_last_name_input().fill(last_name)
        with allure.step("Enter email"):
            registration_page.get_email_input().fill(email)
        with allure.step("Enter password and confirm password"):
            registration_page.get_password_input().fill(password)
            registration_page.get_confirm_password_input().fill(password)
        with allure.step("Submit the registration form"):
            registration_page.get_signup_button().click()

    return _fill_form

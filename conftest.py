import pytest
from playwright.sync_api import sync_playwright
from registration1 import RegistrationPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def wd(page):
    wd = RegistrationPage(page)
    wd.page.goto('https://guest:welcome2qauto@qauto2.forstudy.space/')
    wd.page.wait_for_load_state('networkidle')
    wd.page.locator(".hero-descriptor_btn.btn.btn-primary").click()
    return wd


@pytest.fixture
def fill_registration_form(page):
    def _fill_form(first_name, last_name, email, password):
        registration_page = RegistrationPage(page)
        page.goto('https://guest:welcome2qauto@qauto2.forstudy.space/')
        page.wait_for_load_state('networkidle')
        page.locator(".hero-descriptor_btn.btn.btn-primary").click()

        registration_page.get_first_name_input().fill(first_name)
        registration_page.get_last_name_input().fill(last_name)
        registration_page.get_email_input().fill(email)
        registration_page.get_password_input().fill(password)
        registration_page.get_confirm_password_input().fill(password)

        registration_page.get_signup_button().click()

    return _fill_form

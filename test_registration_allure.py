import pytest
import allure
from faker import Faker


def test_registration_2(wd, fill_registration_form):
	fake = Faker()
	first_name = "TestUser"
	last_name = "User"
	email = fake.email(domain='example.com')
	password = "Password123"
	fill_registration_form(first_name, last_name, email, password)
	assert wd.page.url == "https://guest:welcome2qauto@qauto2.forstudy.space/"


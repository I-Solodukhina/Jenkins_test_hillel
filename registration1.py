class RegistrationPage:
    def __init__(self, page):
        self.page = page

    def get_first_name_input(self):
        return self.page.locator('#signupName')

    def get_last_name_input(self):
        return self.page.locator('#signupLastName')

    def get_email_input(self):
        return self.page.locator('#signupEmail')

    def get_password_input(self):
        return self.page.locator('#signupPassword')

    def get_confirm_password_input(self):
        return self.page.locator('#signupRepeatPassword')

    def get_signup_button(self):
        return self.page.locator("button[class='btn btn-primary']")

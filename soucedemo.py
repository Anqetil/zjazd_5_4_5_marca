# Page Objcet Model

class LoginPage:
    def __init__(self, okno_przegladarki):
        self.driver = okno_przegladarki
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'


class LoginPageLocators:
    LANGUAGES_SELECT = "xpath=//select[@id='languages']"
    USERNAME_INP = "xpath=//input[@name='username']"
    PASSWORD_INP = "xpath=//input[@name='password']"

    LOGIN_BTN = "xpath=//button[@id='login-button']"
    LOGO_LOGIN_PAGE = "xpath=//*[@name='login']/descendant::img"

    WRONG_CREDS_ALERT = "xpath=//scrm-message-ui/descendant::div[@role='alert']"

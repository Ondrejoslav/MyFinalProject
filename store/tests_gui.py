from django.test import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class GuiTestWithSelenium(TestCase):

    def test_home_page_firefox(self):
        selenium_webdriver = webdriver.Firefox()
        selenium_webdriver.get('http://127.0.0.1:8000/')
        assert 'Welcome to our laboratory glassware store!' in selenium_webdriver.page_source

    def test_home_page_edge(self):
        selenium_webdriver = webdriver.Edge()
        selenium_webdriver.get('http://127.0.0.1:8000/')
        assert 'Welcome to our laboratory glassware store!' in selenium_webdriver.page_source

    def test_signup(self):
        selenium_webdriver = webdriver.Edge()
        selenium_webdriver.get('http://127.0.0.1:8000/accounts/signup/')
        username_field = selenium_webdriver.find_element(By.ID, 'id_username')
        username_field.send_keys('TestUser')
        first_name_field = selenium_webdriver.find_element(By.ID, 'id_first_name')
        first_name_field.send_keys('Name')
        last_name_field = selenium_webdriver.find_element(By.ID, 'id_last_name')
        last_name_field.send_keys('Surname')
        email_field = selenium_webdriver.find_element(By.ID, 'id_email')
        email_field.send_keys('email@seznam.cz')
        password1_field = selenium_webdriver.find_element(By.ID, 'id_password1')
        password1_field.send_keys('SDdk5!a@')
        password2_field = selenium_webdriver.find_element(By.ID, 'id_password2')
        password2_field.send_keys('SDdk5!a@')
        phone_number_field = selenium_webdriver.find_element(By.ID, 'id_phone_number')
        phone_number_field.send_keys('0548651257')
        date_of_birth_field = selenium_webdriver.find_element(By.ID, 'id_date_of_birth')
        date_of_birth_field.send_keys('06-05-2010')
        billing_address_field = selenium_webdriver.find_element(By.ID, 'id_billing_address')
        billing_address_field.send_keys('some text.')
        submit_button = selenium_webdriver.find_element(By.ID, 'id_submit')
        submit_button.send_keys(Keys.RETURN)

        assert 'Welcome to our laboratory glassware store!' in selenium_webdriver.page_source
        #assert 'A user with that username already exists.' in selenium_webdriver.page_source # if repeated once more

    def test_signup_2(self):
        selenium_webdriver = webdriver.Edge()
        selenium_webdriver.get('http://127.0.0.1:8000/accounts/signup/')
        username_field = selenium_webdriver.find_element(By.ID, 'id_username')
        username_field.send_keys('TestUser1')
        first_name_field = selenium_webdriver.find_element(By.ID, 'id_first_name')
        first_name_field.send_keys('Name')
        last_name_field = selenium_webdriver.find_element(By.ID, 'id_last_name')
        last_name_field.send_keys('Surname')
        email_field = selenium_webdriver.find_element(By.ID, 'id_email')
        email_field.send_keys('email@seznam.cz')
        password1_field = selenium_webdriver.find_element(By.ID, 'id_password1')
        password1_field.send_keys('SDdsk5!dfa@')
        password2_field = selenium_webdriver.find_element(By.ID, 'id_password2')
        password2_field.send_keys('Ssk5!dfa@')
        phone_number_field = selenium_webdriver.find_element(By.ID, 'id_phone_number')
        phone_number_field.send_keys('0548651257')
        date_of_birth_field = selenium_webdriver.find_element(By.ID, 'id_date_of_birth')
        date_of_birth_field.send_keys('06-05-2010')
        billing_address_field = selenium_webdriver.find_element(By.ID, 'id_billing_address')
        billing_address_field.send_keys('some text.')
        submit_button = selenium_webdriver.find_element(By.ID, 'id_submit')
        submit_button.send_keys(Keys.RETURN)

        assert 'The two password fields didn’t match.' in selenium_webdriver.page_source

    def test_signup_3(self):
            selenium_webdriver = webdriver.Edge()
            selenium_webdriver.get('http://127.0.0.1:8000/accounts/signup/')
            username_field = selenium_webdriver.find_element(By.ID, 'id_username')
            username_field.send_keys('TestUser2')
            first_name_field = selenium_webdriver.find_element(By.ID, 'id_first_name')
            first_name_field.send_keys('Name2')
            last_name_field = selenium_webdriver.find_element(By.ID, 'id_last_name')
            last_name_field.send_keys('Surname2')
            email_field = selenium_webdriver.find_element(By.ID, 'id_email')
            email_field.send_keys('email@seznam.cz')
            password1_field = selenium_webdriver.find_element(By.ID, 'id_password1')
            password1_field.send_keys('SDdsk5!dfa@')
            password2_field = selenium_webdriver.find_element(By.ID, 'id_password2')
            password2_field.send_keys('SDdsk5!dfa@')
            phone_number_field = selenium_webdriver.find_element(By.ID, 'id_phone_number')
            phone_number_field.send_keys('0548651257')
            date_of_birth_field = selenium_webdriver.find_element(By.ID, 'id_date_of_birth')
            date_of_birth_field.send_keys('06-08-2024')
            billing_address_field = selenium_webdriver.find_element(By.ID, 'id_billing_address')
            billing_address_field.send_keys('some text.')
            submit_button = selenium_webdriver.find_element(By.ID, 'id_submit')
            submit_button.send_keys(Keys.RETURN)

            assert 'Only past dates are allowed!' in selenium_webdriver.page_source



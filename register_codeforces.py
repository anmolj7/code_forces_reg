from selenium.webdriver import Chrome 
import time 
import os 
from getpass import getpass
import re 


class Register:
    def __init__(self):
        self.handle = input("Enter the handle: ")
        self.email = input("Enter the email: ")
        assert self.is_valid(self.email), "Email is not valid."
        self.password = getpass('Enter the password: ')
        self.confirm_password = getpass("Retype the password: ")

        if self.password != self.confirm_password:
            print("The entered passwords don't match.")
        else:
            self.enter_details() 
    
    def slow_typing(self, browser_element, text, wait_time=0.07):
        for char in text:
            browser_element.send_keys(char)
            time.sleep(wait_time)

    def enter_details(self):
        browser = Chrome()
        browser.get('https://www.codeforces.com/register')

        self.slow_typing(browser.find_element_by_name('handle'), self.handle)
        self.slow_typing(browser.find_element_by_name('email'), self.email)
        self.slow_typing(browser.find_element_by_name('password'), self.password)
        self.slow_typing(browser.find_element_by_name('passwordConfirmation'), self.password)

        browser.find_element_by_class_name('submit').click()
        time.sleep(5)
        if browser.title == 'Register - Codeforces':
            print("There was something wrong with the information you provided. Make sure that the password is a strong one and of atleast 5 characters, and the email and handle are not already in use.")
        if browser.title == "Successfully Registered - Codeforces":
            print('Successfully registered! Open email to verify!')


    def is_valid(self, email):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(regex, email):
            return True 
        else:
            return False


def main():
    Register()

if __name__ == "__main__":
    main()
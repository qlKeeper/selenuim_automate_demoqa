from selenium.webdriver.common.by import By
from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import CheckBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person
import random


class TextBoxPage(BasePage):
    
    URL = 'https://demoqa.com/text-box'
    
    locators = TextBoxPageLocators()

    
    def fill_all_fields(self):
        full_name = next(generated_person()).full_name
        email = next(generated_person()).email
        current_address = next(generated_person()).current_address
        permament_address = next(generated_person()).permament_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMAMENT_ADDRESS).send_keys(permament_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permament_address
    
    def check_filled_form(self):
       full_name = self.element_is_present\
        (self.locators.CREATED_FULL_NAME).text.split(':')[1]
       
       email = self.element_is_present\
        (self.locators.CREATED_EMAIL).text.split(':')[1]
       
       current_address = self.element_is_present\
        (self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
       
       permament_address = self.element_is_present\
        (self.locators.CREATED_PERMAMENT_ADDRESS).text.split(':')[1]
       
       return full_name, email, current_address, permament_address
    

class CheckBoxPage(BasePage):

    URL = 'https://demoqa.com/checkbox'

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BTN).click()

    def click_random_checkbox(self):
        item_list = self.all_elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count > 0:
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()
            count -= 1


    def get_checked_checkbox(self):
        checked_list = self.all_elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.', '').replace('doc', '').lower()


    def get_output_result(self):
        result_list = self.all_elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(' ', '')
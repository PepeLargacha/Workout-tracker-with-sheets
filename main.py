"""main"""
from brain import post_row_to_sheets, get_data_form_nutrix

user_input = input('Describe your workout today: ')

post_row_to_sheets(get_data_form_nutrix(user_input))

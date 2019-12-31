# content of test_strings.py
import logging

def test_valid_string(stringinput):
    logging.info(stringinput)
    logging.info(stringinput['word'])
    assert stringinput['word'].isalpha()
    

def test_new_case(stringinput):
    logging.info(stringinput)
    logging.info(stringinput['new_test'])
    assert stringinput['new_test'].isalpha()
import logging
from fixt import *
# def setup_function(function):
    # #logging.info(dir(function))
    # logging.info(function.__module__)
    # #logging.info(dir(function.__module__))
    # function.answer = 17
    # logging.info("Setup " + str(function.answer))

# def teardown_function(function):
    
    # if function.answer:
        # logging.info("teardown Worked")
    # del function.answer 
    # # if answer in function:
        # # logging.info("teardown Worked")

def test_modlevel(test_input):
    #assert modlevel[0] == 42
    logging.info("inside test test_modlevel")
    logging.info(test_input)
    #assert test_modlevel.answer == 17
   
def test_modlevel2(test_input):
    #assert modlevel[0] == 42
    assert False, "Faile"
    logging.info("inside test test_modlevel2")
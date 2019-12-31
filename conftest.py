import logging
a =  {
    "test_valid_string":[{
        "word": "Test"
    },{
        "word": "Testnew"
    }],
    "test_new_case": {
        "new_test": "Manoj"
    }
}

def pytest_generate_tests(metafunc):
    logging.info(dir(metafunc.module))
    logging.info(metafunc.module.__name__)
    #logging.info(metafunc.function.__name__)
    if "stringinput" in metafunc.fixturenames:
        #logging.info(a[metafunc.function.__name__])
        metafunc.parametrize("stringinput", read_json(metafunc.function.__name__))


def read_json(method_name):
    if type(a[method_name]) == list:
        return a[method_name]
    else:
        return [a[method_name]]
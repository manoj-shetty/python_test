import logging
import pytest
import os

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

# @pytest.fixture
# def test():
    # print("test_call")
    # return "Manoj"

# def pytest_generate_tests(metafunc):
    # logging.info(dir(metafunc.module))
    # logging.info(metafunc.module.__name__)
    # #logging.info(metafunc.function.__name__)
    # if "stringinput" in metafunc.fixturenames:
        # #logging.info(a[metafunc.function.__name__])
        # metafunc.parametrize("stringinput", read_json(metafunc.function.__name__))


# def read_json(method_name):
    # if type(a[method_name]) == list:
        # return a[method_name]
    # else:
        # return [a[method_name]]

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="session", autouse=True)
def set_test_path(request):
    logging.info('\n-----------------')
    logging.info('fixturename : %s' % request.fixturename)
    logging.info('scope       : %s' % request.scope)
    #logging.info('function    : %s' % request.function.__name__)
    #logging.info('cls         : %s' % request.cls)
    #logging.info('module      : %s' % request.module.__name__)
    #logging.info('fspath      : %s' % request.fspath)
    logging.info('fspath      : %s' % dir(request))
    logging.info(os.path.abspath(__file__))
    logging.info('-----------------')
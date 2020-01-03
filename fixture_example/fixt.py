import pytest
import logging
import json
import traceback


a = {}

@pytest.fixture(autouse=True)
#def test_input(request, record_xml_attribute):
def test_input(request, record_property):
    # Code that will run before your test, for example:
    # logging.info('\n-----------------')
    # logging.info('fixturename : %s' % request.fixturename)
    # logging.info('scope       : %s' % request.scope)
    # logging.info('function    : %s' % request.function.__name__)
    # logging.info('cls         : %s' % request.cls)
    # logging.info('module      : %s' % request.module.__name__)
    # logging.info('fspath      : %s' % request.fspath)
    # logging.info('-----------------')

    logging.info(request.module.__name__)
    logging.info(request.function.__name__)
    logging.info("files_before = # ... do something to check the existing files")
    # A test function will be run at this point
    with open('tmp.json') as jsn:
        a = json.load(jsn)
    try:
        yield [a[request.function.__name__],a[request.function.__name__]]
        logging.info("no exception")
    except:
        logging.debug("Trace: " + traceback.format_exc())
        raise
    

    # Code that will run after your test, for example:
    logging.info("files_after = # ... do something to check the existing files")
    #assert files_before == files_after
    # if request.node.rep_setup.failed:
        # #logging.info("setting up a test failed!", request.node.nodeid)
        # pass
    # elif request.node.rep_setup.passed:
    if request.node.rep_call.failed:
        logging.info("executing test failed")
        record_property("test_result", "FAIL")
        #record_xml_attribute("result", "FAIL")
        #logging.info("executing test failed", request.node.nodeid)

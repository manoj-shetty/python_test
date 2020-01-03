import pprint
a = {
    "test_doc_processing_for_all_doc_types": {
        "request_data.file_path": "MSA_Test_doc.docx",
        "request_data.file_path_new.test": "MSA_Test_doc.docx",
        "request_data.file_path_new.test1": "MSA_Test_doc.docx",
        "request_data.ntest.test1": "MSA_Test_doc.docx",
        "expected_response.status" : "FINISHED"
    }
}

resp_json = {'request_data': {}, 'expected_response': {}}
for key, value in a['test_doc_processing_for_all_doc_types'].items():
    # print("******************")
    # print("******************")
    # print(key + " : " + value)
    # print("******************")
    # print("******************")
    tmp_json = resp_json
    parent_key = None
    last_key = None
    for each_key in key.split('.'):
        # print(tmp_json)
        parent_json = tmp_json
        if each_key not in tmp_json:
            tmp_json[each_key] = {}
            tmp_json = tmp_json[each_key]
        else:
            tmp_json = tmp_json[each_key]
        last_key = each_key
    parent_json[last_key] = value

pprint.pprint(resp_json)
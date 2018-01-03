def create_instance(incoming_data):
    from parser import HttpRequestParser
    return HttpRequestParser.parse(incoming_data)

import json


def json_decoder(parameter_to_parser):

    body_parser = parameter_to_parser.decode('utf-8')

    body = json.loads(body_parser)

    return body
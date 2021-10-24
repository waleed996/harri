"""
Utility functions related to client requests

"""


def get_query_param_or_default(request, key, default):
    """Get value from query params of a GET request

    Args:
        request ([WSGIRequest]): [The GET request made by the client]
        key ([str]): [The key whose value is to be get from the request query params]
        default ([obj]): [The default value to return in case given key is not found]

    Returns:
        [value or default]: [Returns the value of the key from query params or default]
    """


    if key in request.query_params:
        key = request.query_params.get(key)
        if key:
            return key
    return default
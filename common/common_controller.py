"""
Controllers related to common functionality of the project
are contained here

"""


from utils.response_utils import create_response, create_message


class CommonController:
    """Controller class for the common app"""


    def hello_world(self, request):
        """Hello World method docs

        Args:
            request ([WSGIRequest]): [The HTTP Request made by the client]
        """

        try:

            return create_response(create_message("HELLO HARRI!", 1000), 200)


        except Exception as ex:
            print(ex)



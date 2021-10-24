"""
All common views related to the project are contained here

"""


from rest_framework.views import APIView

from common.common_controller import CommonController


class CommonView(APIView):
    """Common view for Hello World"""


    common_controller = CommonController()


    def get(self, request):
        """GET http request view"""

        return self.common_controller.hello_world(request)


    def post(self, reuqest):
        """POST http request view"""

        pass


    def patch(self, request):
        """PATCH http request view"""

        pass


    def delete(self, request):
        """DELETE http request view"""

        pass


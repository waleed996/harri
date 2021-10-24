"""
Utility functions for server response messages

"""


import json
import os

from harri.settings import SERVER_MSG_LOCALE


def get_message(msg_code=None):
    """Get localized server message according to the given code.
    Locale used is configured in settings

    Args:
        msg_code ([int], mandatory): [Message code described in module locale]
    """

    try:

        # msg_code not provided
        if not msg_code:
            raise ValueError("msg_code not provided")

        # Open server messages file
        with open(
            os.path.dirname(os.path.realpath(__file__)) + "/message.json", "r"
        ) as message_file:

            message_dict = json.load(message_file)

            return message_dict[str(msg_code)]["msg"][SERVER_MSG_LOCALE]

    except Exception as ex:
        return "Message not found against code " + str(msg_code)


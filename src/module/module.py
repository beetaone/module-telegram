"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
import os
import requests

log = getLogger("module")

MESSAGE_LABEL = os.getenv("MESSAGE_LABEL")
URL = f"https://api.telegram.org/bot{os.getenv('TOKEN')}/sendMessage?chat_id={os.getenv('CHAT_ID')}&text="

def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Sending data to Telegram ...")

    try:
        # YOUR CODE HERE
        resp = requests.get(URL + received_data[MESSAGE_LABEL]).json()

        if not resp['ok']:
            return f"Error when sending data to Discord channel. Server response: {resp}"

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"

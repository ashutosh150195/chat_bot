from __future__ import print_function
from sn import service_now
import requests
#from clientname import user_name

import os
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

    import apiai

# demo agent acess token: e5dc21cab6df451c866bf5efacb40178

CLIENT_ACCESS_TOKEN = '76a42f10cb364e9e8284175131ad6f17'
information = []


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    while True:
        print(u"> ", end=u"")
        user_message = input()
        information.append(user_message)
        print(information)

        if user_message == u"exit":
            break

        request = ai.text_request()
        request.query = user_message

        response = json.loads(request.getresponse().read())

        result = response['result']
        action = result.get('action')
        actionIncomplete = result.get('actionIncomplete', False)

        print(u"< %s" % response['result']['fulfillment']['speech'])
        # cd=response['result']['fulfillment']['speech']
        # print("-----------"+cd)

        if action is not None:
            if action == u"send_message":
                parameters = result['parameters']

                text = parameters.get('text')
                message_type = parameters.get('message_type')
                parent = parameters.get('parent')

                print (
                    'text: %s, message_type: %s, parent: %s' %
                    (
                        text if text else "null",
                        message_type if message_type else "null",
                        parent if parent else "null"
                    )
                )

                if not actionIncomplete:
                    print(u"...Sending Message...")
                    break

if __name__ == '__main__':
    main()
    #user_name(information)
    service_now(information)


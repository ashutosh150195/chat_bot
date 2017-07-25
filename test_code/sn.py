#Need to install requests package for python
#easy_install requests
import requests


def service_now(information):
   # Set the request parameters
    url = 'https://dev39753.service-now.com/api/now/table/incident?sysparm_display_value='

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = '2TtsK8wMsKKd89a'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    #response = requests.get(url, auth=(user, pwd), headers=headers )
    response = requests.post(url, auth=(user, pwd), headers=headers,
                             data="{\"short_description\":\"" + information[1] + "\","
                             "\"caller_id\":\"" + information[2] + "\", \"comments\":\"Testing going on\"}")

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
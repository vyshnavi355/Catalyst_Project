from flask import Request, jsonify, make_response
import requests
import json
import zcatalyst_sdk
url = "https://commerce.zoho.in/store/api/v1/products"   # Zoho Commerce API URL
def handler(request: Request):  #The handler function takes a Flask Request object as a parameter.
    try:
        app = zcatalyst_sdk.initialize()  # Initializing Catalyst SDK
        accesstoken = fetchaccesstoken(app) #he function retrieves the access token for the Zoho Commerce API.
        print("The value of access token is")
        print(accesstoken)
        #Payload
        req_data = request.get_json ()# The JSON data from the request is retrieved.
        payload = req_data.get('request') #The payload for the API request is extracted from the JSON data.
        print("The payload is")
       
        # Headers for the API request
        headers = {
                'Authorization': 'Zoho-oauthtoken '+accesstoken,
                'X-com-zoho-store-organizationid': '60026223176',
                'Content-Type': 'application/json',
                    }

            # The POST request is made to the Zoho Commerce API with the specified headers and payload.
            #Send an HTTP POST request to a specified URL.
        print(payload)
        res = requests.post(url, headers=headers, json=payload)
            # If the response is successful, a JSON response is returned to the client.
            # Otherwise, an error message is returned.
        if res.status_code == 201:
                print("Successfully created Products.")
                response = make_response(jsonify({
                "message": res.text
            }), res.status_code)
                return response
        else: #Error Handling 
                print(f"Error: {res.status_code} - {res.text}")
                response = make_response(jsonify({
                "message": res.text
            }), res.status_code)
                return response 

    except Exception as e: # Exception Handling.
        print(f"An error occurred: {str(e)}")

def fetchaccesstoken(app):    # Configuring and getting access token using the Zoho Console
        connector = app.connection({
            'ConnectorName': {
            'client_id': '1000.6KCPBDCG3ZHTXNQK39LWJFHJ086DTY',
            'client_secret': '44efef815461f661e34c9abbcff6ebe4e4b91ee171',
            'auth_url': 'https://accounts.zoho.in/oauth/v2/token',
            'refresh_url': 'https://accounts.zoho.in/oauth/v2/token',
            'refresh_token': '1000.23e53669389f40b69f4e24416b083003.ba8c6a45f7e4d2ec3e86eddd6d6f61fe' #never expired
            }
            }).get_connector('ConnectorName')
        access_token = connector.get_access_token() # Getting and printing the access token
        print(access_token)
        return access_token  
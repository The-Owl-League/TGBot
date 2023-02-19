import requests

def send_request(userid):
    endpoint_url = "http://185.104.248.207:6079/v1/users/search"
    
    response = requests.get(endpoint_url)
    data=[]

    if response.status_code == 200:
        response_data = response.json()
    else:
        print(f"Error: {response.status_code}")
        
    print (response_data)
        
    for fetchedid in response_data:
        print(fetchedid['id'])
        print(userid)
        if int(fetchedid['id']) == int(userid):
            data.append(fetchedid['id'])
            data.append(fetchedid['telegram_id'])
            return data
    if data == []:
        return 'error'
        
        
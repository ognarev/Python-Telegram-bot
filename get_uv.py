import requests
import json

def get_uv(longitude, latitude, header, token):
    '''Returns formated json with information from openuv.io'''
    openUV_url = 'https://api.openuv.io/api/v1/uv'
    place_data = {'lng': longitude, 'lat': latitude}
    openUV_headers = {header: token}
    reader = requests.get(openUV_url, headers=openUV_headers, params=place_data)
    uv_dict = reader.json()
    return json.dumps(uv_dict, indent=4, sort_keys=True)

# with open('.sensdata/openuv.json') as reader:
#     data = json.load(reader)
#     header = data['header']
#     token = data['token']
    
# print(get_uv(115.67, -31.45, header, token))
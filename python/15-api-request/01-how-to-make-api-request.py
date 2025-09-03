import requests

base_url="https://jsonplaceholder.typicode.com"

def get_api_info(end_point):
    complete_url=f"{base_url}/{end_point}"
    try:
       response=requests.get(complete_url)
       response.raise_for_status()
       results_obj=response.json()
       print("results ",results_obj)
    except requests.RequestException as e:
        print("Error fetching data ",e)
get_api_info('comments')
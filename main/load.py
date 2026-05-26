import requests

def load_ticket(data):

    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=data
    )

    return response.status_code
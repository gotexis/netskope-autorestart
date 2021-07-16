import requests

def has_access():
    try:
        response = requests.get(
            'https://ci.9msn.net/login.html',
            verify=False,
            timeout=5
        )
        if response.status_code == 200:
            return True
    except requests.exceptions.Timeout:
        ...
    return False


import requests

# Just demo API
def update_product_from_api(url, payload):
    response = requests.get(url, data=payload)
    status_code, text = response.status_code, response.text
    # or use response.json() if json serializable
    return (status_code, text)

import requests

url = "https://air-10.dev.ascensor.co.uk/about"

urlStatus = requests.get(url).status_code
print(urlStatus)

if urlStatus != 200:
    print(f"Status code for {url} = {urlStatus}.")
else:
    print("Status code 200.")
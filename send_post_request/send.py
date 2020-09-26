## with this py file I tested my service-counter
import requests
r = requests.post("http://0.0.0.0:80/post")
print(r.text) # displays the result body.

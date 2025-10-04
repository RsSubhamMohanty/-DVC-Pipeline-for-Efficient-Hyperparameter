import json
import requests

url = "http://localhost:8000/predict"

x_new = dict (
    ph = 10.71608,
    Hardness = 500.89045,
    Solids = 20791.318981,
    Chloramines = 7.300212,
    Sulfate = 368.516441,
    Conductivity = 564.308654,
    Organic_carbon = 10.3797783,
    Trihalomethanes = 86.99097,
    Turbidity = 2.963135
)

response = requests.post(url, json=x_new)


print("Response.text:",response.text)
print("Status code:", response.status_code)

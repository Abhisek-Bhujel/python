import json
import urllib.request

json_data_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json'

# with open('temperature_anomaly.json', encoding='utf-8') as data:
#     anomalies = json.load(data)

with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)
    
print(anomalies)
print(f"description {anomalies['description']}")

for year, value in anomalies['data'].items():
    print(f"{int(year)} ......{float(value) : 6.2f}")
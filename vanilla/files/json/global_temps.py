import json

with open('temperature_anomaly.json', encoding='utf-8') as data:
    anomalies = json.load(data)
    
# print(anomalies)
print(f"description {anomalies['description']}")
print(f"citation {anomalies['citation']}")

for year, value in anomalies['data'].items():
    print(f"{int(year)} ......{float(value) : 6.2f}")
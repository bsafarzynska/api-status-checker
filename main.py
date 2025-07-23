import requests
import csv

with open('urls.txt', 'r') as f:
    urls = [line.strip() for line in f.readlines() if line.strip()]

results = []

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        results.append([url, response.status_code])
    except Exception as e:
        results.append([url, f'Error: {e}'])

with open('raport.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['URL', 'Status'])
    writer.writerows(results)

print("Status report saved to raport.csv")

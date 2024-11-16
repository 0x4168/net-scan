import csv
import json    

def save_results_csv(results):
    with open("scan_results.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["IP", "Port", "CVE ID", "Severity", "Description"])
        writer.writeheader()
        for result in results:
            writer.writerow(result)

def save_results_json(results):
    with open("scan_results.json", "w") as jsonfile:
        json.dump(results, jsonfile, indent=4)

def save_results_html(results):
    with open("scan_results.html", "w") as htmlfile:
        htmlfile.write("<html><body><h1>Scan Results : </h1><ul>")
        for result in results:
            htmlfile.write(f"<li><b>-- IP: {result['IP']}</b> -- <br><br><b>Port:</b> {result['Port']} <br><b>CVE:</b> {result['CVE ID']}<br><b>Description:</b> {result['Description']}<br><b>Severity:</b> {result['Severity']}<br><b>Default : {result['Default']}</b><br><b>Password : {result['Password']}</b><br><b>Username : {result['Username']}</b><br><br></li>")
        htmlfile.write("</ul></body></html>")
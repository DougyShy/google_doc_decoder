import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# Find all tables - Standard Table Grab for a published Google Doc
tables = soup.find_all("table")

# Collect all cells (skipping header) - IF HEADERS EXIST - THE EXERCISE WAS NOT SPECIFIC
doc_rows = []
for table in tables:
    rows = table.find_all("tr")
    for row in rows[1:]:  # skip header row
        cells = row.find_all(["td", "th"])
        for cell in cells:
            content = cell.get_text(strip=True)
            if content:
                doc_rows.append(content)

# Group cells by threes
parsed_google_doc = [doc_rows[i:i+3] for i in range(0, len(doc_rows), 3)]


def decode_google_doc(doc):
  max_rows = len(doc)
  print(max_rows)
  for row in doc:
    print (row)

decode_google_doc(parsed_google_doc)

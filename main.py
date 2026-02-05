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
custom_parsed_google_doc = [doc_rows[i:i+3] for i in range(0, len(doc_rows), 3)]

# DECODE AND ULTIMATELY SET UP THE DRAWING OF GRID ENCRYPTED MESSAGE
def decode_google_doc(doc):
  number_of_rows_left = max(int(row[2]) for row in doc)
  # - DEBUG/TESTING - print("number of rows left" + str(number_of_rows_left))

  # swap grid logic to make it easier to traverse
  for row in doc:
    row[0], row[2] = row[2], row[0]
  # sort for same reason
  doc.sort(key=lambda r: (-int(r[0]), int(r[2])))

  # create individual rows to build words
  row_text = ''

  for current_row in range(number_of_rows_left, -1, -1):
      line = ''
      for row in doc:
          if int(row[0]) == current_row:
              line += row[1]  # keep building row string
      row_text += line + '\n'  # to start a new line

  print(row_text)

# THIS IS THE ASSIGNMENT - ASSUMING ALL GOOGLE PUBLISHED URLs HAVE A HEADER ROW
decode_google_doc(parsed_google_doc)

# THIS IS TRIAL AND ERROR/DESIGN - IT INCORPORATES MORE THAN JUST ONE LETTER FROM THE EXAMPLE IF THIS IS THE FORMAT USED
def load_custom_parsed(doc):
    doc.append(['4', ' ', '2'])
    doc.append(['5', '█', '2'])
    doc.append(['6', '▀', '2'])
    doc.append(['7', '▀', '2'])
    doc.append(['8', '█', '2'])
    doc.append(['3', ' ', '1'])
    doc.append(['4', ' ', '1'])
    doc.append(['5', '█', '1'])
    doc.append(['6', '▀', '1'])
    doc.append(['7', '█', '1'])
    doc.append(['8', '▀', '1'])

    doc.append(['1', ' ', '0'])
    doc.append(['2', ' ', '0'])
    doc.append(['3', ' ', '0'])
    doc.append(['4', ' ', '0'])
    doc.append(['5', '█', '0'])
    doc.append(['6', ' ', '0'])
    doc.append(['7', ' ', '0'])
    doc.append(['8', '█', '0'])

    doc.append(['9', ' ', '2'])
    doc.append(['9', ' ', '1'])
    doc.append(['9', ' ', '0'])

    doc.append(['10', '█', '2'])
    doc.append(['11', ' ', '2'])
    doc.append(['12', ' ', '2'])
    doc.append(['13', '█', '2'])
    doc.append(['10', '▀', '1'])
    doc.append(['11', '█', '1'])
    doc.append(['12', '█', '1'])
    doc.append(['13', '▀', '1'])
    doc.append(['10', ' ', '0'])
    doc.append(['11', '█', '0'])
    doc.append(['12', '█', '0'])
    doc.append(['13', ' ', '0'])
    
# ELABORATE ON ORIGINAL LETTER TO FORM A WORD
load_custom_parsed(custom_parsed_google_doc)
# CHECK TO SEE IF WORD APPEARS SUCCESSFULLY WITH NEW CUSTOM GOOGLE PUB - * THE WORD 'FRY' SHOULD BE LEGIBLE INSTEAD OF JUST AN 'F'
decode_google_doc(custom_parsed_google_doc)

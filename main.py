import requests
from bs4 import BeautifulSoup

trial_url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

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
# Sort by x-coord
parsed_google_doc.sort(key=lambda x: (int(x[0]), int(x[2])))
# Swap x and y coords for actual screen writing and easier understanding
for row in parsed_google_doc:
    row[0], row[2] = int(row[2]), int(row[0])
# Sort for same reason
parsed_google_doc.sort(key=lambda r: (-int(r[0]), int(r[2])))


def decode_google_doc(doc):
    #for row in doc:
    #    print(row)
    number_of_rows = max(int(row[0]) for row in doc)
    print(f'Number of rows left = {number_of_rows}')
    # - DEBUG/TESTING - print("number of rows left" + str(number_of_rows_left))
    max_chars_per_row = max(int(row[2]) for row in doc)
    print(f'Max characters per line: {max_chars_per_row}')
    number_of_coords = len(doc)
    print(f'Number of coords: {number_of_coords}')

    line = ''
    line_rows = ''

    
    current_index = -1
    for y in range (number_of_rows, -1, -1):
        current_index += 1
        for x in range (0, max_chars_per_row -1):
            print(y, x)
            print(current_index)
            if doc[current_index][0] == y and doc[current_index][2] == x:
                print("match")
                line += doc[current_index][1]
                current_index += 1
            else:
                line += ' '
        print(line)
        line_rows += line + '\n'
        line = ''
        print(f'Current index: {current_index}')
        print(f'Number of coords: {number_of_coords}')
        

    print(line_rows)

    # ONLY GET TWO LINE UP TOP - BELOW WORKS - RESEARCH IT

    '''coord_map = {(int(r), int(c)): ch for r, ch, c in doc}

    text = ""
    for y in range(number_of_rows, -1, -1):
        line = ""
        for x in range(max_chars_per_row):
            line += coord_map.get((y, x), " ")
        text += line + "\n"

    print(text)'''
        
    
decode_google_doc(parsed_google_doc)
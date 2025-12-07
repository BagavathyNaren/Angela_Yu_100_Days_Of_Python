import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    url = "https://flavorsofcacao.com/database_w_REF.html"

    # 1. Download page
    resp = requests.get(url)
    resp.raise_for_status()          # raises if request failed

     # 2. Parse HTML
    soup = BeautifulSoup(resp.text, "lxml")

     # 3. Find the table by id (see HTML)
    table = soup.find("table", id="choco_database")

     # 4. Extract headers
    header_cells = table.find("tr").find_all("th")
    headers = [h.get_text(strip=True) for h in header_cells]

     # 5. Extract data rows
    rows = []
    for tr in table.find_all("tr")[1:]:        # skip header row
        cells = tr.find_all(["td", "th"])
        if not cells:
           continue
        row = [td.get_text(strip=True) for td in cells]
    # skip completely empty rows
        if any(row):
           rows.append(row)

    # 6. Create DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # 7. Save to CSV
    df.to_csv("flavors_of_cacao.csv", index=False, encoding="utf-8")

    print("Saved", len(df), "rows")

except Exception as e:
    print(f"Error: {e}")
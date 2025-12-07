import streamlit as st
import pandas as pd
import requests

URL = "https://min-api.cryptocompare.com/data/top/totalvolfull?limit=100&tsym=USD"

@st.cache_data(ttl=120)
def get_data(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json().get("Data", [])
        return data
    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
        return []

def format_money(value):
    if value is None:
        return "N/A"

    if value < 1:
        return f"${value:.6f}"

    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    if value >= 1_000:
        return f"${value / 1_000:.2f}K"

    return f"${value:.2f}"

def get_dataframe(data):
    rows = []
    for item in data:
        coin = item.get("CoinInfo", {})
        raw = item.get("RAW", {}).get("USD", {})

        price = raw.get("PRICE")
        open_24h = raw.get("OPEN24HOUR")

        if price is None or open_24h is None or open_24h == 0:
            continue

        change_24h = price - open_24h
        pct_24h = (change_24h / open_24h) * 100

        rows.append({
            "Symbol": coin.get("Name"),
            "Full Name": coin.get("FullName"),
            "Image URL": (
                "https://www.cryptocompare.com" + coin.get("ImageUrl")
                if coin.get("ImageUrl") else None
            ),
            "Price": price,
            "Percent Change 24h": pct_24h,
            "Market Cap": raw.get("MKTCAP"),
        })

    return pd.DataFrame(rows)

data = get_data(URL)
df = get_dataframe(data)

st.title("Top Crypto Gainers & Losers (24h)")

def display_table(title, frame):
    st.subheader(title)

    for _, row in frame.iterrows():
        cols = st.columns([1, 2, 4, 2, 2])
        with cols[0]:
            if row["Image URL"]:
                st.image(row["Image URL"], width=40)
        with cols[1]:
            st.write(row["Symbol"])
        with cols[2]:
            st.write(row["Full Name"])
        with cols[3]:
            st.write(format_money(row["Price"]))
        with cols[4]:
            pct = row["Percent Change 24h"]
            st.write(f"{pct:.2f}%")

gainers = df.sort_values("Percent Change 24h", ascending=False).head(10)
losers = df.sort_values("Percent Change 24h", ascending=True).head(10)

display_table("Top Gainers", gainers)
display_table("Top Losers", losers)

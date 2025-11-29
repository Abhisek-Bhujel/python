import requests
import tkinter as tk
import time

def get_crypto_prices():
    url_crypto = "https://api.coingecko.com/api/v3/coins/markets"
    params_crypto = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }
    data = requests.get(url_crypto, params=params_crypto).json()

    # Currency conversion API
    fx_data = requests.get("https://open.er-api.com/v6/latest/USD").json()
    usd_to_npr = fx_data["rates"]["NPR"]

    result = []
    for coin in data:
        name = coin["name"]
        usd_price = coin["current_price"]
        npr_price = round(usd_price * usd_to_npr, 2)
        result.append(f"{name}:  USD ${usd_price} | NPR ₹{npr_price}")
    return "   |   ".join(result)


def scroll_text():
    global text, x
    canvas.delete("all")
    canvas.create_text(x, 30, text=text, fill="white", font=("Consolas", 14))

    x -= 2  
    if x < -len(text) * 7:  # reset for smooth scrolling
        x = window.winfo_width()

    canvas.after(50, scroll_text)  # speed control

def update_prices():
    global text
    text = get_crypto_prices()
    window.after(10000, update_prices)  # update every 10 sec


# GUI Window
window = tk.Tk()
window.title("Crypto Price Ticker")
window.configure(bg="black")

canvas = tk.Canvas(window, width=900, height=60, bg="black", highlightthickness=0)
canvas.pack()

x = 900
text = get_crypto_prices()

scroll_text()
update_prices()

window.mainloop()

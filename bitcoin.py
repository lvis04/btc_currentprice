import requests 
import tkinter as tk
from datetime import datetime 
#####

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().strftime("%d/%m/%y")
    
    labelPrice.config(text=f"{price:,.2f} $")
    labelTime.config(text= f"Updated at: {time}")
    labelDate.config(text= f"Today: {date}")    
    
    canvas.after(1000, trackBitcoin)
    
canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title('Bitcoin Current Price')

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text = "Bitcoin Price", font = f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font = f3)
labelTime.pack (pady=20)

labelDate = tk.Label(canvas, font=f3)
labelDate.pack(pady=20)

trackBitcoin()

canvas.mainloop()


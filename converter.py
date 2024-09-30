import tkinter as tk
from tkinter import font
from tkinter import ttk
import requests

root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x300")
root.configure(bg="black")

API_KEY = '0c3635e71350668974f71d9a'  # ExchangeRate-API key

API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"

def submit():
    try:
        base_currency = cur1.get()
        dest_currency = cur2.get()
        amount = amount1.get()
        if base_currency and dest_currency and amount > 0:
            # Use the new API
            response = requests.get(f"{API_URL}/{base_currency}/{dest_currency}")
            data = response.json()
            if data['result'] == 'success':
                rate = data['conversion_rate']
                amt2.delete("1.0", tk.END)
                converted_amount = amount * rate
                amt2.insert(tk.END, f"{converted_amount:.2f}")
            else:
                amt2.delete("1.0", tk.END)
                amt2.insert(tk.END, "API Error")
        else:
            amt2.delete("1.0", tk.END)
            amt2.insert(tk.END, "Invalid Input")
    except Exception as e:
        amt2.delete("1.0", tk.END)
        amt2.insert(tk.END, f"Error: {str(e)}")

# window and canvas 
canvas = tk.Canvas(root, width=500, height=300, bg="black")
canvas.create_rectangle(10, 10, 490, 290, fill="lightgreen")
canvas.create_rectangle(25, 10, 475, 50, outline="black", fill="green")

# custom font
custom_font = font.Font(family="Baskerville Old Face", size=20, weight="bold")
custom_font2 = font.Font(family="Baskerville Old Face", size=14, weight="bold")
custom_font3 = font.Font(family="Baskerville Old Face", size=10, weight="bold")
canvas.create_text(250, 30, text="CURRENCY CONVERTER", font=custom_font, fill="black")

# design
## left side line-polygon
canvas.create_line(0, 80, 300, 80)
canvas.create_line(0, 180, 200, 180)
canvas.create_line(300, 80, 199, 181)
canvas.create_polygon(0, 70, 300, 70, 200, 170, 0, 170)
## right side line-polygon
canvas.create_line(300, 130, 500, 130)
canvas.create_line(200, 230, 500, 230)
canvas.create_line(300, 130, 200, 230)
canvas.create_polygon(300, 140, 200, 240, 500, 240, 500, 140)

# left menu
canvas.create_text(90, 90, text="Select Currency :", font=custom_font2, fill="white")
cur1 = tk.StringVar()
currency1 = ttk.Combobox(root, width=8, textvariable=cur1)
currency1['values'] = ('USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF')  # Valid currency codes
canvas.create_window(205, 90, window=currency1)
currency1.current(0)

canvas.create_text(82, 120, text="Enter Amount :", font=custom_font2, fill="white")
amount1 = tk.DoubleVar()
amt1 = tk.Entry(root, width=8, textvariable=amount1, font=('calibre', 10, 'normal'))
canvas.create_window(185, 120, window=amt1)

sub_btn = tk.Button(root, width=10, bg="green", fg="white", activebackground="cyan", text='SUBMIT', font=custom_font3, command=submit)
canvas.create_window(80, 150, window=sub_btn)

# right menu
canvas.create_text(320, 220, text="Select Currency :", font=custom_font2, fill="white")
cur2 = tk.StringVar()
currency2 = ttk.Combobox(root, width=8, textvariable=cur2)
currency2['values'] = ('INR', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF')  # Valid currency codes
canvas.create_window(440, 220, window=currency2)
currency2.current(0)

canvas.create_text(340, 180, text="Amount is :", font=custom_font2, fill="white")

amt2 = tk.Text(root, width=8, height=1, font=('calibre', 10, 'normal'))
canvas.create_window(430, 180, window=amt2)

canvas.pack()

root.mainloop()
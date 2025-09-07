import customtkinter as ctk
from calculations import destiny_number, lifepath_number, personal_year, soul_urge_number
from chart import draw_chart

# Настройки на стила
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

# Създаване на основен прозорец
app = ctk.CTk()
app.title("Нумерологичен анализатор")
app.geometry("400x250")

# --- Полета за въвеждане ---
label_name = ctk.CTkLabel(app, text="Въведи пълно име:")
label_name.pack(pady=10)
entry_name = ctk.CTkEntry(app, width=250)
entry_name.pack(pady=5)

label_date = ctk.CTkLabel(app, text="Въведи дата на раждане (ДД.ММ.ГГГГ):")
label_date.pack(pady=10)
entry_date = ctk.CTkEntry(app, width=250)
entry_date.pack(pady=5)

def on_click():
    # Функция, която се извиква при натискане на бутона.
    # 1. Взима данните от input полетата
    # 2. Изчислява всички числа чрез calculations.py
    # 3. Генерира диаграмата чрез chart.py

    name = entry_name.get().upper()
    date = entry_date.get().split('.')

    destiny = destiny_number(name)
    lifepath = lifepath_number(date)
    your_year = personal_year(date)
    soul_number = soul_urge_number(name)

    draw_chart(name, lifepath, soul_number, destiny, your_year)

# --- Бутон ---
button = ctk.CTkButton(app, text="Генерирай диаграма", command=on_click)
button.pack(pady=20)

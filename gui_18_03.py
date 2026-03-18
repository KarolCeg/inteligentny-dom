import tkinter as tk

root = tk.Tk()
root.title("Inteligentny dom")

canvas = tk.Canvas(root, width=820, height=650, bg="white", highlightthickness=0)
canvas.pack(side="left")

panel = tk.Frame(root, width=480, height=650, bg="#f0f0f0")
panel.pack(side="right", fill="both", expand=True)

# dane świateł
swiatla = [
    {"stan": False, "kolor": "yellow", "nazwa": "Żarówka garaż"},
    {"stan": False, "kolor": "yellow", "nazwa": "Żarówka salon"},
    {"stan": False, "kolor": "blue", "nazwa": "Wanna"},
    {"stan": False, "kolor": "yellow", "nazwa": "Żarówka przedpokój"},
     {"stan": False, "kolor": "yellow", "nazwa": "Żarówka łazienka"},
      {"stan": False, "kolor": "yellow", "nazwa": "Żarówka salon"},
]

def przelacz(i):
    swiatla[i]["stan"] = not swiatla[i]["stan"]

    if swiatla[i]["stan"]:
        canvas.itemconfig(swiatla[i]["canvas"], fill=swiatla[i]["kolor"])
        swiatla[i]["button"].config(
            text=f"{swiatla[i]['nazwa']}: WŁĄCZONE",
            bg="#b3ffb3"
        )
    else:
        canvas.itemconfig(swiatla[i]["canvas"], fill="white")
        swiatla[i]["button"].config(
            text=f"{swiatla[i]['nazwa']}: WYŁĄCZONE",
            bg="#ffb3b3"
        )

# rysowanie elementów na canvas
swiatla[0]["canvas"] = canvas.create_oval(120, 300, 170, 350, outline="black", width=2, fill="white") #garaz
swiatla[1]["canvas"] = canvas.create_oval(630, 125, 680, 175, outline="black", width=2, fill="white") #kuchnia
swiatla[2]["canvas"] = canvas.create_oval(260, 100, 300, 200, outline="black", width=2, fill="white") #wanna
swiatla[3]["canvas"] = canvas.create_oval(295, 350, 345, 400, outline="black", width=2, fill="white") #przedpokoj
swiatla[4]["canvas"] = canvas.create_oval(400, 125, 450, 175, outline="black", width=2, fill="white") #lazienka
swiatla[5]["canvas"] = canvas.create_oval(630, 350, 680, 400, outline="black", width=2, fill="white") #salon
# tworzenie przycisków
for i, s in enumerate(swiatla):
    btn = tk.Button(
        panel,
        text=f"{s['nazwa']}: WYŁĄCZONE",
        command=lambda i=i: przelacz(i),
        font=("Arial", 8, "bold"),
        bg="#ffb3b3",
        width=25,
        height=2
    )
    btn.pack(pady=10)
    s["button"] = btn
# grubość ścian
w = 3
# ściany zewnętrzne
canvas.create_line(50, 140, 50, 520, width=w)
canvas.create_line(50, 520, 237, 520, width=w)
canvas.create_line(237, 520, 237, 500, width=w)
canvas.create_line(237, 500, 280, 500, width=w)
canvas.create_line(350, 500, 800, 500, width=w)
canvas.create_line(800, 500, 800, 50, width=w)
canvas.create_line(800, 50, 237, 50, width=w)
canvas.create_line(237, 50, 237, 140, width=w)
canvas.create_line(237, 140, 50, 140, width=w)
# ściany wewnętrzne
canvas.create_line(237, 140, 237, 250, width=w)
canvas.create_line(237, 350, 237, 500, width=w)
canvas.create_line(237, 250, 400, 250, width=w)
canvas.create_line(400, 250, 400, 290, width=w)
canvas.create_line(400, 290, 420, 290, width=w)
canvas.create_line(500, 290, 520, 290, width=w)
canvas.create_line(520, 50, 520, 290, width=w)
canvas.create_line(400, 500, 400, 380, width=w)
# # --- zegar ---
# godziny = 0
# minuty = 0
# sekundy = 0
# # ikona zegara
# zegar_label = tk.Label(root, text="00:00:00", font=("Courier", 36, "bold"), bg="white", fg="black")
# # wspolrzedne
# zegar_label.place(x=30, y=600) 

# def aktualizuj_zegar():
#     global godziny, minuty, sekundy

#     sekundy += 1
#     if sekundy >= 60:
#         sekundy = 0
#         minuty += 1
#         if minuty >= 60:
#             minuty = 0
#             godziny += 1
#             if godziny >= 24:
#                 godziny = 0

#     # wyswietlanie wgui
#     czas_str = f"{godziny:02d}:{minuty:02d}:{sekundy:02d}"
#     zegar_label.config(text=czas_str)

#     # Uruchamia co 1 milisekundę
#     root.after(1, aktualizuj_zegar)
# aktualizuj_zegar()
# #--------koniec zegar--------

# --- zegar z prostokatem  ---
def create_rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1, x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2, x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2, x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)
# tlo zegara
create_rounded_rect(canvas, 30, 540, 300, 620, radius=20, fill="#333333", outline="black")
#tekst zegara
zegar_text_id = canvas.create_text(165, 580, text="00:00:00", fill="white", font=("Courier", 32, "bold"))

# --- logika zegar---
godziny, minuty, sekundy = 0, 0, 0

def aktualizuj_zegar():
    global godziny, minuty, sekundy
    sekundy += 1
    if sekundy >= 60:
        sekundy = 0
        minuty += 1
        if minuty >= 60:
            minuty = 0
            godziny += 1
            if godziny >= 24:
                godziny = 0

    czas_str = f"{godziny:02d}:{minuty:02d}:{sekundy:02d}"
    # aktualizacja tekstu
    canvas.itemconfig(zegar_text_id, text=czas_str)
    root.after(1, aktualizuj_zegar)

aktualizuj_zegar()
# #--------koniec zegar--------
root.mainloop()

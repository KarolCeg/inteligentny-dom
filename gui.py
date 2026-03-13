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
    {"stan": False, "kolor": "blue", "nazwa": "Wanna"}
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
swiatla[0]["canvas"] = canvas.create_oval(120, 300, 170, 350, outline="black", width=2, fill="white")
swiatla[1]["canvas"] = canvas.create_oval(630, 125, 680, 175, outline="black", width=2, fill="white")
swiatla[2]["canvas"] = canvas.create_oval(260, 100, 300, 200, outline="black", width=2, fill="white")


# tworzenie przycisków
for i, s in enumerate(swiatla):

    btn = tk.Button(
        panel,
        text=f"{s['nazwa']}: WYŁĄCZONE",
        command=lambda i=i: przelacz(i),
        font=("Arial", 12, "bold"),
        bg="#ffb3b3",
        width=25,
        height=2
    )

    btn.pack(pady=30)
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

root.mainloop()

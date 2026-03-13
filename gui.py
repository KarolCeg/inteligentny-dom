import tkinter as tk

root = tk.Tk()
root.title("Inteligentny dom")


stan_swiatla = tk.BooleanVar(value=False)

def przelacz():
    # Pobieramy aktualną wartość i ustawiamy odwrotną
    nowy_stan = not stan_swiatla.get()
    stan_swiatla.set(nowy_stan)
    

    #zarowka - zmiana koloru
    kolor = "yellow" if stan_swiatla.get() else "white"
    canvas.itemconfig(zarowka, fill=kolor)

    # Aktualizacja wyglądu przycisku/etykiety w zależności od zmiennej
    if stan_swiatla.get():
        przycisk.config(text="ŚWIATŁO: WŁĄCZONE", bg="#b3ffb3")
    else:
        przycisk.config(text="ŚWIATŁO: WYŁĄCZONE", bg="#ffb3b3")


canvas = tk.Canvas(root, width=820, height=650, bg="white", highlightthickness=0)
canvas.pack(side="left")

panel = tk.Frame(root, width=480, height=650, bg="#f0f0f0")
panel.pack(side="right", fill="both", expand=True)

# Przycisk w panelu bocznym
przycisk = tk.Button(
    panel, 
    text="ŚWIATŁO: WYŁĄCZONE", 
    command=przelacz, 
    font=("Arial", 12, "bold"),
    bg="#ffb3b3",
    width=25,
    height=2
)
przycisk.pack(pady=50) 

w = 3  # Grubość linii
#budynek 
#implementacja zmiennej sygnalizujacej stan
zarowka = canvas.create_oval(120, 300, 170, 350, outline="black", width=2, fill="white")
# sciany zewnetrzne
canvas.create_line(50, 140, 50, 520, width=w)
canvas.create_line(50, 520, 237, 520, width=w)
canvas.create_line(237, 520, 237, 500, width=w)

canvas.create_line(237, 500, 280, 500, width=w)
canvas.create_line(350, 500, 800, 500, width=w)
canvas.create_line(800, 500, 800, 50, width=w)
canvas.create_line(800, 50, 237, 50, width=w)
canvas.create_line(237, 50, 237, 140, width=w)
canvas.create_line(237, 140, 50, 140, width=w)

# Ściany wewnętrzne
canvas.create_line(237, 140, 237, 250, width=w) 
canvas.create_line(237, 350, 237, 500, width=w)
canvas.create_line(237, 250, 400, 250, width=w) 
canvas.create_line(400, 250, 400, 290, width=w) 
canvas.create_line(400, 290, 420, 290, width=w) 
canvas.create_line(500, 290, 520, 290, width=w) 
canvas.create_line(520, 50, 520, 290, width=w) 
canvas.create_line(400, 500, 400, 380, width=w)

root.mainloop()

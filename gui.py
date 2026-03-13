import tkinter as tk

root = tk.Tk()
root.title("Inteligetny dom")

canvas = tk.Canvas(root, width=1300, height=650, bg="white")
canvas.pack()

w = 3  # Grubość linii

# --- ZARYS ZEWNĘTRZNY ---

canvas.create_line(50, 140, 50, 520, width=w)
canvas.create_line(50, 520, 237, 520, width=w)
canvas.create_line(237, 520, 237, 500, width=w)

canvas.create_line(237, 500, 800, 500, width=w)

canvas.create_line(800, 500, 800, 50, width=w)

canvas.create_line(800, 50, 237, 50, width=w)

canvas.create_line(237, 50, 237, 140, width=w)

canvas.create_line(237, 140, 50, 140, width=w)


canvas.create_line(237, 140, 237, 250, width=w) 
canvas.create_line(237, 350, 237, 500, width=w)

canvas.create_line(237, 250, 400, 250, width=w) 
canvas.create_line(400, 250, 400, 290, width=w) 
canvas.create_line(400, 290, 420, 290, width=w) 
canvas.create_line(500, 290, 520, 290, width=w) 

canvas.create_line(520, 50, 520, 290, width=w)  

canvas.create_line(400, 500, 400, 380, width=w)

root.mainloop()

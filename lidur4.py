import random
import tkinter as tk

# Taka inn afmælisdaga hópsins
dd = int(input("Afmælisdagur: "))   
mm = int(input("Afmælismánuður: "))  
yyyy = int(input("Fæðingarár: "))   

seed = int(f"{dd:02d}{mm:02d}{yyyy}")
random.seed(seed)

# Búa til 4x4 fylki
matrix_size = 4
matrix = [[random.randint(0, 1) for _ in range(matrix_size)] for _ in range(matrix_size)]

formatted_date = f"{dd:02d}-{mm:02d}-{yyyy}"

print(f"Fylki fyrir dagsetningu {formatted_date} með seed {seed}:")
for row in matrix:
    print(row)
print()

# Eiginleikar venslanna
def sjalfhverft(matrix):
    for i in range(matrix_size):
        if matrix[i][i] != 1: 
            return False
    return True

def samhverft(matrix):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] != matrix[j][i]: 
                return False
    return True

def andsamhverft(matrix):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:  
                return False
    return True

def gegnvirkt(matrix):
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] != 1:  
                    return False
    return True

print("Eiginleikar venslanna")
print(f"Sjálfhverf: {sjalfhverft(matrix)}")
print(f"Samhverft: {samhverft(matrix)}")
print(f"Andsamhverft: {andsamhverft(matrix)}")
print(f"Gegnvirk: {gegnvirkt(matrix)}")

# Teikna örvanet til að sýna venslin
def teikna_orva(matrix):
    root = tk.Tk()
    root.title("Örvanet fyrir vensl")

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    coordinates = {
        0: (100, 100),
        1: (300, 100),
        2: (100, 300),
        3: (300, 300)
    }

    # Teikna hnúta
    for i, (x, y) in coordinates.items():
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue")
        canvas.create_text(x, y, text=str(i + 1), font=("Arial", 12, "bold"))

    # Teikna örvar
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] == 1:
                x1, y1 = coordinates[i]
                x2, y2 = coordinates[j]

                # Teikna örvar milli hnúta
                if i != j:
                    canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
                else:  # Teikna loop ör
                    canvas.create_arc(x1 - 30, y1 - 30, x1 + 30, y1 + 30, start=0, extent=300, style=tk.ARC)

    # Sýna gluggann
    root.mainloop()

teikna_orva(matrix)

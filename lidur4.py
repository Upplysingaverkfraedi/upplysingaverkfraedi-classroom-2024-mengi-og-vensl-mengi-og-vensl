import numpy as np
import matplotlib.pyplot as plt


# Function to generate the relation matrix and analyze it based on a date
def generate_relation(dd, mm, yyyy, n=4):
    # Búa til slembifræ út frá dagsetningunni
    seed = int(f"{dd:02d}{mm:02d}{yyyy}")
    np.random.seed(seed)

    # Búa til slembifylki af stærð n x n með 0 eða 1
    relation_matrix = np.random.randint(0, 2, size=(n, n))

    # Endirskrifa dagsetninguna á formið "dd-mm-yyyy"
    formatted_date = f"{dd:02d}-{mm:02d}-{yyyy}"

    # Prenta niðurstöður
    print(f"Fylkið fyrir dagsetninguna {formatted_date} og seed {seed}:")
    print(relation_matrix)
    print()

    # Check properties of the relation
    print("Sjálfhverft (Reflexive):", check_reflexive(relation_matrix))
    print("Samhverft (Symmetric):", check_symmetric(relation_matrix))
    print("Andsamhverft (Antisymmetric):", check_antisymmetric(relation_matrix))
    print("Gegnvirkt (Transitive):", check_transitive(relation_matrix))

    # Sýna venslin myndrænt
    draw_relation(relation_matrix)


# Function to check if the matrix is reflexive
def check_reflexive(matrix):
    for i in range(matrix.shape[0]):
        if matrix[i, i] != 1:
            return False
    return True


# Function to check if the matrix is symmetric
def check_symmetric(matrix):
    return np.all(matrix == matrix.T)


# Function to check if the matrix is antisymmetric
def check_antisymmetric(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i != j and matrix[i, j] == 1 and matrix[j, i] == 1:
                return False
    return True


# Function to check if the matrix is transitive
def check_transitive(matrix):
    n = matrix.shape[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i, j] == 1 and matrix[j, k] == 1 and matrix[i, k] != 1:
                    return False
    return True


# Function to visualize the relation matrix
def draw_relation(matrix):
    plt.figure(figsize=(8, 8))

    theta = np.linspace(0, 2 * np.pi, matrix.shape[0], endpoint=False)
    x = np.cos(theta)
    y = np.sin(theta)

    for i in range(matrix.shape[0]):
        plt.text(x[i], y[i], str(i), ha='center', va='center', fontsize=20,
                 bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='circle,pad=0.5'))

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 1:
                dx = x[j] - x[i]
                dy = y[j] - y[i]
                plt.arrow(x[i], y[i], 0.85 * dx, 0.85 * dy, head_width=0.05, head_length=0.1,
                          fc='black', ec='black', length_includes_head=True)

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.axis('off')
    plt.show()


# Dæmi um notkun
dd = int(input("Sláðu inn dagsetningu fæðingardags (1-31): "))
mm = int(input("Sláðu inn mánuð fæðingardags (1-12): "))
yyyy = int(input("Sláðu inn ár fæðingardags (t.d., 1990): "))

generate_relation(dd, mm, yyyy)

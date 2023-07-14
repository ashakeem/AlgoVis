import tkinter as tk
import random
import time

# Create the main window
root = tk.Tk()
root.title("Algorithm Visualizer")
root.geometry("800x600")

# Global variables
data = []
algorithm_names = ["Merge Sort (O(n log n))", "Quick Sort (O(n log n))", "Dijkstra's Algorithm (O(V^2 + E))"]

# Function to generate random data
def generate_data():
    global data
    data = random.sample(range(1, 100), 50)
    draw_data(data, "Generated Data")

# Function for Merge Sort
def merge_sort():
    merge_sort_helper(data, 0, len(data) - 1)
    draw_data(data, "Merge Sort (O(n log n))")

def merge_sort_helper(data, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort_helper(data, low, mid)
        merge_sort_helper(data, mid + 1, high)
        merge(data, low, mid, high)

def merge(data, low, mid, high):
    left = data[low:mid+1]
    right = data[mid+1:high+1]
    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1

    draw_data(data)
    time.sleep(0.1)  # Delay between each step

# Function for Quick Sort
def quick_sort():
    quick_sort_helper(data, 0, len(data) - 1)
    draw_data(data, "Quick Sort (O(n log n))")

def quick_sort_helper(data, low, high):
    if low < high:
        pivot = partition(data, low, high)
        quick_sort_helper(data, low, pivot - 1)
        quick_sort_helper(data, pivot + 1, high)

def partition(data, low, high):
    pivot = data[high]
    i = low - 1

    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw_data(data)
            time.sleep(0.1)  # Delay between each step

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

# Function for Dijkstra's Algorithm
def dijkstras_algorithm():
    draw_data(data, "Dijkstra's Algorithm (O(V^2 + E))")

# Function to draw the data on the canvas
def draw_data(data, algorithm=""):
    canvas.delete("all")
    bar_width = 10
    bar_distance = 5
    max_height = 500
    x = (canvas.winfo_width() - (bar_width + bar_distance) * len(data)) // 2

    for i, height in enumerate(data):
        x0 = x + i * (bar_width + bar_distance)
        y0 = canvas.winfo_height() - height * (max_height / max(data))
        x1 = x0 + bar_width
        y1 = canvas.winfo_height()
        canvas.create_rectangle(x0, y0, x1, y1, fill="sky blue")
        canvas.create_text(x0 + 2, y0 - 15, anchor=tk.SW, text=str(height))

    canvas.create_text(canvas.winfo_width() // 2, 30, anchor=tk.N, text=algorithm, font=("Arial", 14, "bold"))
    canvas.update()
    time.sleep(0.1)  # Delay between each step

# Create the canvas
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()

# Create the buttons
button_generate = tk.Button(root, text="Generate Data", command=generate_data)
button_generate.pack(side=tk.LEFT, padx=10, pady=10)

button_merge_sort = tk.Button(root, text="Merge Sort", command=merge_sort)
button_merge_sort.pack(side=tk.LEFT, padx=10, pady=10)

button_quick_sort = tk.Button(root, text="Quick Sort", command=quick_sort)
button_quick_sort.pack(side=tk.LEFT, padx=10, pady=10)

button_dijkstra = tk.Button(root, text="Dijkstra's Algorithm(COMING SOON!)", command=dijkstras_algorithm)
button_dijkstra.pack(side=tk.LEFT, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()

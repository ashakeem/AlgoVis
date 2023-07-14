# Algorithm Visualizer

This program demonstrates the visualization of various algorithms using the Tkinter library in Python.


![Project demo](https://github.com/ashakeem/AlgorithmVisualizerPython/assets/125868067/c107235a-416d-4e05-952c-b58fccf142fe)

## Getting Started

To run the program, make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

### Prerequisites

This program requires the `tkinter` library, which is included in the standard library of Python.

### Installation

No installation is required as the `tkinter` library comes pre-installed with Python.

## Running the Program

To run the program, follow these steps:

1. Save the code provided in a file with a `.py` extension (e.g., `algorithm_visualizer.py`).

2. Open a terminal or command prompt and navigate to the directory where the file is saved.

3. Execute the following command to run the program:

   ```bash
   python algorithm_visualizer.py
   ```

## Program Explanation

The program uses Tkinter to create a graphical user interface (GUI) for the algorithm visualizer.

### Algorithm Selection

The program provides three algorithms to visualize:

1. Merge Sort
2. Quick Sort
3. Dijkstra's Algorithm

### Generate Data

Clicking the "Generate Data" button generates a random list of 50 integers between 1 and 100. This data will be used for the algorithms' visualization.

### Merge Sort

Clicking the "Merge Sort" button triggers the visualization of the Merge Sort algorithm. The implementation of Merge Sort is recursive and divides the data into smaller sublists until they are sorted individually. Then, the sorted sublists are merged to obtain the final sorted list.

### Quick Sort

Clicking the "Quick Sort" button triggers the visualization of the Quick Sort algorithm. Quick Sort is also a recursive algorithm that works by selecting a pivot element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

### Dijkstra's Algorithm

Clicking the "Dijkstra's Algorithm" button (currently marked as "COMING SOON!") will trigger the visualization of Dijkstra's Algorithm. This algorithm is used to find the shortest path between nodes in a graph. However, the implementation of this algorithm is not provided in the code.

### Visualizing the Algorithms

The program uses a canvas widget to display the data visually. Each element in the data list is represented by a rectangle on the canvas. The height of the rectangle corresponds to the value of the element.

The visualization is updated step-by-step to demonstrate the progress of the algorithm. A delay of 0.1 seconds is introduced between each step to make the visualization more apparent.

## Contributing

Contributions to this project are welcome. If you have any suggestions or improvements, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.

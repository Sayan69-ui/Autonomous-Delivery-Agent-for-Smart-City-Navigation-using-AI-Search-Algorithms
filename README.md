## 🚚 Autonomous Delivery Agent for Smart City Navigation using AI Search Algorithms
## 🚚 Autonomous Delivery Agent (AI Project)

---

## 📌 Overview

This project implements an autonomous delivery agent that navigates a smart city environment using Artificial Intelligence (AI) search algorithms.

The system simulates a grid-based city with obstacles, traffic zones, and user-defined start and goal points. It provides real-time visualization of pathfinding and explains why different algorithms choose specific routes.

---

## 🌍 Real-World Motivation

With the rapid growth of delivery services such as Amazon, Swiggy, and Zomato, efficient route planning has become a critical challenge.

Delivery agents must:

* Avoid obstacles (buildings, blocked paths)
* Handle traffic congestion
* Minimize travel time and cost

This project demonstrates how AI can be used to solve such real-world navigation problems.

---

## 🧠 Algorithms Implemented

### 🔵 Breadth-First Search (BFS)

* Finds shortest path in terms of steps
* Does NOT consider terrain cost
* Can lead to inefficient routes

### 🟡 Uniform Cost Search (UCS)

* Considers movement cost
* Finds optimal (lowest-cost) path
* Explores more nodes

### 🔴 A* Search Algorithm

* Uses heuristic (Manhattan Distance)
* Combines cost + heuristic
* Fastest and most efficient

---

## 🗺️ Environment Design

The environment is represented as a 2D grid:

| Symbol | Meaning             | Cost    |
| ------ | ------------------- | ------- |
| `.`    | Road                | 1       |
| `W`    | Traffic Zone        | 5       |
| `#`    | Building (Obstacle) | Blocked |

Features:

* Complex city layout
* Narrow paths and obstacles
* Weighted terrain

---

## 🎮 Features

✅ Interactive GUI using Tkinter

✅ User-defined Start and Goal (mouse click)

✅ Dynamic obstacle placement

✅ Real-time path animation

✅ Algorithm comparison

✅ Explanation panel displaying:

* Total cost
* Nodes explored
* Reason behind path selection

---

## 🖥️ User Interface

The system provides a grid-based visual interface:

* 🟢 Green → Start point
* 🔴 Red → Goal
* ⚫ Black → Obstacles
* 🟠 Orange → Traffic zones
* 🔵 Blue → Agent path

---

## 🖱️ Controls

### 🖱️ Mouse Controls

* **Left Click**

  * First click → Set Start point
  * Second click → Set Goal point

* **Right Click**

  * Toggle obstacle (add/remove buildings)

---

### 🔘 Button Controls

* **BFS Button**

  * Runs Breadth-First Search
  * Finds shortest path in terms of steps

* **UCS Button**

  * Runs Uniform Cost Search
  * Finds lowest-cost path considering terrain

* **A*  Button**

  * Runs A* Search
  * Uses heuristic + cost for fastest optimal path

* **Reset Button**

  * Clears start, goal, and resets the map

---

## ▶️ How to Run

### 🔧 Prerequisites

Make sure you have the following installed:

* Python 3.x
* Git (optional, for cloning the repository)

---

### 📥 Step 1: Get the Project

**Option 1: Clone using Git**

```bash
git clone https://github.com/Sayan69-ui/Autonomous-Delivery-Agent-for-Smart-City-Navigation-using-AI-Search-Algorithms.git
cd Autonomous-Delivery-Agent-for-Smart-City-Navigation-using-AI-Search-Algorithms
```

**Option 2: Download ZIP**

* Go to the GitHub repository
* Click on **Code → Download ZIP**
* Extract the folder

---

### ▶️ Step 2: Run the Application

```bash
python main.py
```

---

### 🖥️ Step 3: Use the Application

* Click on the grid to set:

  * Start position (first click)
  * Goal position (second click)

* Use buttons:

  * **BFS / UCS / A*** → Run algorithms
  * **Reset** → Clear map

* Right-click to add/remove obstacles

---

### ⚠️ Notes

* Make sure all project files are in the same folder
* If `python` doesn’t work, try:

```bash
python3 main.py
```

---

## 📊 Output & Analysis

The system provides:

* Path visualization
* Total path cost
* Nodes explored
* Algorithm explanation

### 🔍 Observations:

* BFS → shortest path but ignores cost
* UCS → optimal cost but slower
* A* → optimal and efficient

---

## ⚙️ System Architecture

The project consists of:

* **Environment Module** → Grid, obstacles, terrain
* **Agent Module** → Planning and execution
* **Search Algorithms Module** → BFS, UCS, A*
* **UI Module (Tkinter)** → Visualization

---

## ⚠️ Challenges Faced

* Designing realistic grid environment
* Handling weighted terrain
* Integrating algorithms with GUI
* Visualizing real-time movement

---

## 🚀 Future Scope

* Dynamic moving obstacles (vehicles 🚗)
* Real-world map integration
* Multi-agent delivery systems
* AI-based traffic prediction

---

## 🧑‍💻 Author

**Sayan Bhowmik (25BAI11042)**

CSE (AI & ML)

VIT Bhopal

---

## ⭐ Acknowledgment

This project was developed as part of the **Fundamentals of AI & ML (BYOP)** course.

---

## 💡 Key Takeaway

This project demonstrates how AI search algorithms can solve real-world navigation problems and highlights the importance of heuristics in improving efficiency.

---

# Hospital Simulation Project

This project is a simulation of hospital operations using **SimPy**, designed to analyze patient flows, resource utilization, and service efficiency. It features various performance metrics such as patient wait times, process times, and heatmaps of service usage over time.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Metrics](#key-metrics)
- [Screenshots](#screenshots)
- [License](#license)

---

## Features
- **Patient Simulation**: Models the flow of patients through registration, consultation, and other hospital services.
- **Dynamic Resource Allocation**: Manages resources like doctors, registration counters, and X-ray rooms dynamically.
- **Performance Metrics**:
  - Average wait times for patients and services.
  - Resource utilization over time.
  - Patient flow heatmap for visualizing system bottlenecks.
  - Number of patients in the system over time.
- **Interactive Visualization**: Generates dynamic plots for performance analysis.
- **Web UI**: A simple Flask-based web interface for running simulations.

---

## Technologies Used
- **Python**: Core programming language for the simulation.
- **SimPy**: Discrete-event simulation library.
- **Matplotlib**: Plotting library for generating graphs.
- **Seaborn**: Heatmap visualization.
- **Flask**: Web framework for building the interactive UI.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/hospital-simulation.git
   cd hospital-simulation

2. Set up a virtual environment(If needed):
    python3 -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows

3. pip install -r requirements.txt

4. Run the flask app
    python3 app.py


## Usage

1. Open your browser and navigate to http://127.0.0.1:5000.
2. Enter the input parameters (e.g., number of patients, available resources, etc.).
3. Run the simulation and view the results, including:
    - Wait times and process times.
    - Patient flow heatmap.
    - Avg Wait time and process time per service.
    - Num of visits per service.


## Acknowledgments
1. The SimPy library for simplifying event-based simulations.
2. Matplotlib and Seaborn for visualization.
3. Flask for creating a lightweight web application.


## Results

# Patient Flow Simulation

This project simulates patient flow through a hospital system using SimPy and provides various visualizations for analysis.

---

## Visualizations

### 1. Average Service Times Per Service
![Average Service Times Per Service](https://raw.githubusercontent.com/nikhilteja824/Hospital_ED_Simulation/master/static/results/average_service_times_per_service.jpeg)

---

### 2. Average Wait Times Per Service
![Average Wait Times Per Service](https://raw.githubusercontent.com/nikhilteja824/Hospital_ED_Simulation/master/static/results/average_wait_times_per_service.jpeg)

---

### 3. Patient Flow Heatmap
![Patient Flow Heatmap](https://raw.githubusercontent.com/nikhilteja824/Hospital_ED_Simulation/master/static/results/patient_flow_heatmap.jpeg)

---

### 4. Number of Visits Per Service
![Number of Visits Per Service](https://raw.githubusercontent.com/nikhilteja824/Hospital_ED_Simulation/master/static/results/num_visits_per_service.jpeg)

---

### 5. Patients in System Over Time
![Patients in System Over Time](https://raw.githubusercontent.com/nikhilteja824/Hospital_ED_Simulation/master/static/results/patients_in_system.jpeg)

---

### 6. Processing Times
![Processing Times](https://raw.githubusercontent.com/nikhilteja824/Hospital_ED_Simulation/master/static/results/processing_times.jpeg)

---

### 7. Wait Times
![Wait Times](https://raw.githubusercontent.com/nikhilteja824/Hospital_ED_Simulation/master/static/results/wait_times.jpeg)
---

## Raw Data Files

In addition to the visualizations, raw data files are available for further analysis:
- `flow_data.csv`: Detailed patient flow data in CSV format.
- `flow_data.json`: Detailed patient flow data in JSON format.
- `logs.txt`: Log file with simulation details.
- `service_times_per_process.txt`: Service times for each process.
- `visits_per_service.txt`: Number of visits for each service.
- `wait_times_per_process.txt`: Wait times for each process.

---





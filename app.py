import os
import pandas as pd
from flask import Flask, render_template, request, url_for
from simulation import run_simulation

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/results"

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        # Get form data
        inputs = {
            "NUM_PATIENTS": int(request.form["num_patients"]),
            "NUM_REGISTRATION_COUNTERS": int(request.form["num_registration_counters"]),
            "NUM_DOCTORS": int(request.form["num_doctors"]),
            "NUM_PHARMACY_COUNTERS": int(request.form["num_pharmacy_counters"]),
            "NUM_BILLING_COUNTERS": int(request.form["num_billing_counters"]),
            "NUM_XRAY_COUNTERS": int(request.form["num_xray_counters"]),
            "NUM_SCAN_COUNTERS": int(request.form["num_scan_counters"]),
            "NUM_BEDSPACES": int(request.form["num_bedspaces"]),
        }

        # Ensure static results folder exists
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

        # Run simulation
        simulation_results = run_simulation(inputs, current_index=0)

        # Move plots to the static folder for rendering
        plot_paths = {}
        for plot_name, plot_path in simulation_results["plots"].items():
            if plot_path:
                new_path = os.path.join(app.config["UPLOAD_FOLDER"], os.path.basename(plot_path))
                os.rename(plot_path, new_path)
                plot_paths[plot_name] = url_for('static', filename=os.path.relpath(new_path, "static"))

        # Move logs to the static folder
        logs_path = os.path.join(app.config["UPLOAD_FOLDER"], os.path.basename(simulation_results["logs"]))
        os.rename(simulation_results["logs"], logs_path)
        logs_url = url_for('static', filename=os.path.relpath(logs_path, "static"))

        # Move CSV to the static folder for accessibility
        csv_path = simulation_results["flow_data_csv"]
        if csv_path and os.path.exists(csv_path):
            new_csv_path = os.path.join(app.config["UPLOAD_FOLDER"], os.path.basename(csv_path))
            os.rename(csv_path, new_csv_path)
            csv_url = url_for('static', filename=os.path.relpath(new_csv_path, "static"))
        else:
            csv_url = None

        # Load CSV for preview

        csv_preview = None
        if new_csv_path and os.path.exists(new_csv_path):
            try:
                csv_preview = pd.read_csv(new_csv_path).head(5).to_dict(orient="records")
            except Exception as e:
                print(f"Error reading CSV: {e}")

        logs_url = url_for('static', filename=os.path.relpath(logs_path, "static"))
        # Prepare results dictionary
        # Define service labels
        services = ['Registration', 'Consultation', 'Pharmacy', 'Dressing', 'X-Ray', 'Scan', 'Billing', 'Injection', 'Bed']

        # Include visit counts with corresponding services
        results = {
            "path": simulation_results["path"],
            "flow_data_csv": simulation_results["flow_data_csv"],
            "visit_counts" : simulation_results["visit_counts"],  # Combine service names and counts
            "plots": plot_paths,
            "logs": logs_url,
            "summary": {
                "avg_wait_time": simulation_results["summary"]["avg_wait_time"],
                "max_wait_time": simulation_results["summary"]["max_wait_time"],
                "min_wait_time": simulation_results["summary"]["min_wait_time"],
                "critical_patients": simulation_results["summary"]["critical_patients"],
                "non_critical_patients": simulation_results["summary"]["non_critical_patients"]
            },
            "csv_preview": csv_preview,
        }


    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

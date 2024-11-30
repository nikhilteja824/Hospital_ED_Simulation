import os
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
                plot_paths[plot_name] = os.path.relpath(new_path, "static")

        # Add logs and other results
        logs_path = os.path.join(app.config["UPLOAD_FOLDER"], os.path.basename(simulation_results["logs"]))
        os.rename(simulation_results["logs"], logs_path)

        results = {
            "path": simulation_results["path"],
            "flow_data_csv": simulation_results["flow_data_csv"],
            "visit_counts": simulation_results["visit_counts"],
            "plots": plot_paths,
            "logs": os.path.relpath(logs_path, "static"),
        }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

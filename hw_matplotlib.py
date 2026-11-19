import matplotlib.pyplot as plt
import numpy as np

def load_streamflow(filename):
  """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
  data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=str)
  x_provo = data[:, 0]
  y_provo_1 = data[:, 1].astype(float)
  y_provo_2 = data[:, 2].astype(float)
  y_provo_3 = data[:, 3].astype(float)
  y_provo_4 = data[:, 4].astype(float)
  y_provo_5 = data[:, 5].astype(float)

  dates = x_provo
  flows = np.column_stack([y_provo_1, y_provo_2, y_provo_3, y_provo_4, y_provo_5])
  return dates, flows


def plot_streamflow(dates, flows, sites):
  """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
  x_provo = dates
  y_provo_1 = flows[:, 0]
  y_provo_2 = flows[:, 1]
  y_provo_3 = flows[:, 2]
  y_provo_4 = flows[:, 3]
  y_provo_5 = flows[:, 4]

  plt.figure(figsize=(10, 5))
  plt.plot(x_provo, y_provo_1, label="10163000", color="purple")
  plt.plot(x_provo, y_provo_2, label="10155200", color="teal")
  plt.plot(x_provo, y_provo_3, label="10155500", color="green")
  plt.plot(x_provo, y_provo_4, label="10154200", color="orange")
  plt.plot(x_provo, y_provo_5, label="10155000", color="red")
  plt.xlabel("Date")
  plt.ylabel("Flowrate (cfs)")
  plt.title("Provo River Streamflow Data (2021)")
  plt.legend(title="Site Numbers")
  plt.grid(True)
  plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
  plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates (1).csv")
plot_streamflow(dates, flows, sites)

def summarize(dates, flows, sites):
  # Excel check for gauge 10163000: MAX = [paste Excel MAX], AVERAGE = [paste Excel AVERAGE]
  """Print and save summary statistics (max, date of max, min, average flow) for each gauge."""
  # Print column headers for terminal output
  print(f"{'Gauge':<10} {'Max (cfs)':>10} {'Date of max':<19} {'Min (cfs)':>10} {'Avg (cfs)':>10}")

  # Write summary data to streamflow_summary.csv
  with open("streamflow_summary.csv", "w") as out_file:
    out_file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

    for i, site in enumerate(sites):
      gauge_flows = flows[:, i]
      max_flow = np.max(gauge_flows)
      # Find the row index of the max flow and look up its corresponding date
      max_date = dates[np.argmax(gauge_flows)]
      min_flow = np.min(gauge_flows)
      avg_flow = np.mean(gauge_flows)

      print(f"{site:<10} {max_flow:10.1f} {str(max_date):<19} {min_flow:10.1f} {avg_flow:10.1f}")
      out_file.write(f"{site},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n")

summarize(dates, flows, sites)

# Prompt user for a flow threshold in cfs and convert string input to float
threshold = float(input("Enter a flow threshold (cfs): "))

# Each reading is 15 minutes apart (0.25 hours), so count True values and multiply by 0.25
for i, site in enumerate(sites):
  hours_above = np.sum(flows[:, i] > threshold) * 0.25
  print(f"Gauge {site}: {hours_above:.2f} hours above {threshold} cfs")
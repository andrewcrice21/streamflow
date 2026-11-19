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
  plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates (1).csv")
plot_streamflow(dates, flows, sites)
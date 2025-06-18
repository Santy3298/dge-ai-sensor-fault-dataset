
import pandas as pd
import matplotlib.pyplot as plt

# Load the vibration sensor data
df = pd.read_csv("vibration_data.csv", parse_dates=['timestamp'])

# Plot the vibration signal over time
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['value'], color='blue', linewidth=1.5)
plt.title('Vibration Sensor Readings Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Vibration (g)')
plt.grid(True)
plt.tight_layout()
plt.show()

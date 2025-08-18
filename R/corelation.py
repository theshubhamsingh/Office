import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define correlation matrix
data = np.array([[1, 0.483, 0.680, 0.753, 0.724],
                 [0.483, 1, 0.456, 0.554, 0.418],
                 [0.680, 0.456, 1, 0.673, 0.653],
                 [0.753, 0.554, 0.673, 1, 0.739],
                 [0.724, 0.418, 0.653, 0.739, 1]])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Interpersonal Skills", "Attitude Toward Women Role", 
                                 "Family Support", "Social Activity", "Decision Making"],
                         index=["Interpersonal Skills", "Attitude Toward Women Role", 
                                "Family Support", "Social Activity", "Decision Making"])

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df, annot=True, cmap="coolwarm", linewidths=0.5, vmin=0, vmax=1)
plt.title("Correlation Matrix Heatmap")
plt.show()

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns

# -------------------------------
# Create results folder
# -------------------------------
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# -------------------------------
# Load results
# -------------------------------
df = pd.read_csv("anomaly_results.csv")

# -------------------------------
# Check required columns
# -------------------------------
required_cols = ["label", "is_anomaly", "anomaly_score"]
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}. Please regenerate dataset correctly.")

# -------------------------------
# Prepare labels
# -------------------------------
y_true = df["label"]
y_pred = df["is_anomaly"]

# Convert labels to binary (1 = anomaly, 0 = normal)
y_true_bin = y_true.apply(lambda x: 1 if x == -1 else 0)
y_pred_bin = y_pred.apply(lambda x: 1 if x == -1 else 0)

# -------------------------------
# Print prediction distribution
# -------------------------------
print("\nPrediction Distribution:")
print(df["is_anomaly"].value_counts())

# -------------------------------
# Metrics
# -------------------------------
accuracy = accuracy_score(y_true_bin, y_pred_bin)
precision = precision_score(y_true_bin, y_pred_bin, zero_division=0)
recall = recall_score(y_true_bin, y_pred_bin, zero_division=0)
f1 = f1_score(y_true_bin, y_pred_bin, zero_division=0)

print("\nEvaluation Metrics:")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

# -------------------------------
# Save metrics to file
# -------------------------------
with open(os.path.join(RESULTS_DIR, "metrics.txt"), "w") as f:
    f.write("Evaluation Metrics\n")
    f.write("-------------------\n")
    f.write(f"Accuracy  : {accuracy:.4f}\n")
    f.write(f"Precision : {precision:.4f}\n")
    f.write(f"Recall    : {recall:.4f}\n")
    f.write(f"F1 Score  : {f1:.4f}\n")

# -------------------------------
# Confusion Matrix
# -------------------------------
cm = confusion_matrix(y_true_bin, y_pred_bin)

plt.figure()
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig(os.path.join(RESULTS_DIR, "confusion_matrix.png"))
plt.close()

# -------------------------------
# Anomaly Score Distribution
# -------------------------------
plt.figure()
plt.hist(df["anomaly_score"], bins=50)
plt.title("Anomaly Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.savefig(os.path.join(RESULTS_DIR, "score_distribution.png"))
plt.close()

# -------------------------------
# Scatter Plot (CPU vs Network)
# -------------------------------
plt.figure()

colors = df["is_anomaly"].map({1: "green", -1: "red"})

plt.scatter(
    df["cpu_usage_avg"],
    df["network_out_mb"],
    c=colors
)

plt.xlabel("CPU Usage (%)")
plt.ylabel("Network Out (MB)")
plt.title("CPU vs Network (Anomalies in Red)")

plt.savefig(os.path.join(RESULTS_DIR, "scatter_plot.png"))
plt.close()

# -------------------------------
# Precision vs Recall Bar Plot
# -------------------------------
plt.figure()
metrics = ["Precision", "Recall", "F1 Score"]
values = [precision, recall, f1]

plt.bar(metrics, values)
plt.title("Model Performance Metrics")
plt.ylim(0, 1)

plt.savefig(os.path.join(RESULTS_DIR, "metrics_bar_chart.png"))
plt.close()

print("\n✅ All results saved in 'results/' folder")
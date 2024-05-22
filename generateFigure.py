import torch
import matplotlib.pyplot as plt
data = torch.load("experiments/16_04_2024__22_49_57ECGCNN_M_default_dataset/metrics/Accuracy.pt", map_location="cpu")
plt.figure(figsize=(100, 50))
plt.title("acc")
for i in range(0, len(data)):
    plt.text(i, data[i] + 0.01, round(float(data[i]), ndigits=4), size=5)
plt.plot(data, "o-")
plt.show()
print(max(data))
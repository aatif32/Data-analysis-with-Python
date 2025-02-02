import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Project.csv')

# Line chart: Comparison of expected accuracies for the first 15 data points
plt.figure(figsize=(10, 6))
plt.plot(data['pvalue'][:15], label='pvalue', marker='o')
plt.title('Expected Accuracy Comparison (First 10 Data Points)')
plt.xlabel('Data Point Index')
plt.ylabel('Expected Accuracy')
plt.legend()
plt.grid(True)
plt.show()

# Pie chart: Distribution of the first 15 'latitude' categories
log2FoldChange_counts = data['log2FoldChange'][:15].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(log2FoldChange_counts, labels=log2FoldChange_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('log2FoldChange Distribution (First 5 Data Points)')
plt.show()

# Histogram: Distribution of 'longitude'
plt.figure(figsize=(8, 6))
plt.hist(data['stat'], bins=15, color='blue', edgecolor='black')
plt.title('Distribution of stat')
plt.xlabel('stat')
plt.ylabel('stat Frequency')
#plt.grid(True)
plt.show()

# Scatter plot: Comparison between 'richter' and 'focal_depth'
plt.figure(figsize=(8, 6))
plt.scatter(data['stat'], data['IfcSE'], alpha=0.7, color='red')
plt.title('Scatter Plot: Comparison between stat and IfcSE')
plt.xlabel('stat')
plt.ylabel('IfcSE')
#plt.grid(True)
plt.show()
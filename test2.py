from sklearn.metrics import confusion_matrix
import numpy as np

x_values=[1,2,0,0,1]
y_pred=[2,1,2,0,0]
cm=confusion_matrix(x_values,y_pred)
print(cm)
# Calculate TP, TN, FP, FN for each class
for i in range(len(cm)):
    tp = cm[i, i]
    fn = np.sum(cm[i, :]) - tp
    fp = np.sum(cm[:, i]) - tp
    tn = np.sum(cm) - (tp + fn + fp)
    print(f"\nClass {i}:")
    print(f"True Positives (TP): {tp}")
    print(f"True Negatives (TN): {tn}")
    print(f"False Positives (FP): {fp}")
    print(f"False Negatives (FN): {fn}")
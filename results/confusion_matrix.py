import matplotlib.pyplot as plt  
from sklearn.metrics import roc_curve, ConfusionMatrixDisplay  

# ROC Curve  
fpr, tpr, _ = roc_curve(y_test, y_pred)  
plt.plot(fpr, tpr, label="ROC Curve")  
plt.xlabel("False Positive Rate")  
plt.ylabel("True Positive Rate")  
plt.title("ROC Curve")  
plt.savefig("results/roc_curve.png")  # Save plot  

# Confusion Matrix  
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)  
plt.savefig("results/confusion_matrix.png")  

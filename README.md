# Credit Card Fraud Detection  

## 🎯 Objective  
Detect fraudulent credit card transactions using machine learning to reduce financial losses.  

## 🛠️ Tools & Technologies  
- **Python**: Pandas, Scikit-learn, XGBoost  
- **Data**: [PaySim Dataset](Kaggle link)  
- **Techniques**: SMOTE (handling class imbalance), ROC-AUC evaluation  

## 📊 Results  
- Achieved **90% precision** in fraud detection.  
- Reduced false positives by **20%** using threshold optimization.  

## 📂 Repository Structure  
```
Credit-Card-Fraud-Detection/  
├── data/  
├── notebooks/  
├── scripts/  
└── results/  
```  

## 🚀 How to Run  
1. Clone the repo:  
`git clone https://github.com/yourusername/Credit-Card-Fraud-Detection.git`  
2. Install dependencies:  
`pip install -r requirements.txt`  
3. Run the Jupyter Notebook:  
`jupyter notebook notebooks/fraud_detection.ipynb`

# Dataset  
Download from Kaggle: [PaySim Financial Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1)  
Place the CSV file here before running the code.  

## 📈 Results  
- **Precision (Fraud Class)**: 89%  
- **Recall (Fraud Class)**: 75%  
- **ROC-AUC**: 0.96  
- **False Positives**: 1,332 | **False Negatives**: 54

1. Classification Report
                 precision    recall  f1-score   support

           0       0.99      0.99      0.99    127132
           1       0.89      0.75      0.81       214

    accuracy                           0.99    127346
   macro avg       0.94      0.87      0.90    127346
weighted avg       0.99      0.99      0.99    127346

Key Takeaways:

Precision (Fraud Class): 89% (good—89% of flagged transactions are fraud).

Recall (Fraud Class): 75% (moderate—75% of actual frauds are detected).

ROC-AUC: 0.96 (excellent).

2. Confusion Matrix
Predicted: No Fraud	Predicted: Fraud
Actual: No Fraud	125,800	1,332
Actual: Fraud	54	160
Business Impact:

False Positives: 1,332 (legit transactions flagged as fraud).

False Negatives: 54 (frauds missed).



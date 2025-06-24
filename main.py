#main.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Custom modules
from dataset.data_collection import load_data
from dataset.data_preprocessing import explore_data, checking_removing_duplicates, remove_outliers
from model.model_training import fit_model, train_final_model, save_model
from model.model_testing import classification_metrics, roc_auc_plot

# Step 1: Load data
df = load_data('data/crop.csv')

# Step 2: Explore data
explore_data(df)

# Step 3: Handle duplicates
checking_removing_duplicates(df)

# Step 4: Remove outliers
df_clean = remove_outliers(df)

# Step 5: Prepare training data
target = 'label'
X = df_clean.drop(columns=[target])
y = df_clean[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: train and evaluate multiple models
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

models = [
    ('LR', LogisticRegression()),
    ('LDA', LinearDiscriminantAnalysis()),
    ('KNN', KNeighborsClassifier()),
    ('DT', DecisionTreeClassifier()),
    ('SVM', SVC(probability=True)),
    ('RF', RandomForestClassifier())
]

print("\nTraining base models with cross-validation:")
fit_model(X_train, y_train, models)

# Step 7: train final model
final_model = train_final_model(X_train, y_train)

# Step 8: test the model
y_pred = final_model.predict(X_test)
print("\nEvaluation on validation set:")
classification_metrics(final_model, X_train, X_test, y_train, y_test, y_pred)

# Step 9: ROC Curve
roc_auc_plot(y_test, final_model.predict(X_test))

# Step 10: Save final model
save_model(final_model, 'model/model1.pkl')
print("\n Final model saved as model/model1.pkl")

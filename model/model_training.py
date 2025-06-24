#model/model_training.py
import warnings
import pickle
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

warnings.filterwarnings('ignore')

def read_in_and_split_data(data, target):
    X = data.drop(target, axis=1)
    y = data[target]
    return train_test_split(X, y, test_size=0.2, random_state=0)

def get_models():
    return [
        ('LR', LogisticRegression()),
        ('LDA', LinearDiscriminantAnalysis()),
        ('KNN', KNeighborsClassifier()),
        ('CART', DecisionTreeClassifier()),
        ('SVM', SVC(probability=True)),
    ]

def get_normalized_models(scaler):
    pipelines = []
    for name, model in get_models() + [
        ('AB', AdaBoostClassifier()),
        ('GBM', GradientBoostingClassifier()),
        ('RF', RandomForestClassifier())
    ]:
        pipelines.append((f"{scaler.__class__.__name__}_{name}", Pipeline([
            ('Scaler', scaler),
            (name, model)
        ])))
    return pipelines

def fit_model(X_train, y_train, models):
    results = []
    names = []
    for name, model in models:
        kfold = KFold(n_splits=10, shuffle=True, random_state=0)
        cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')
        results.append(cv_results)
        names.append(name)
        print(f"{name}: {cv_results.mean():.4f} ({cv_results.std():.4f})")
    return names, results

def train_final_model(X_train, y_train):
    pipeline = make_pipeline(MinMaxScaler(), RandomForestClassifier())
    model = pipeline.fit(X_train, y_train)
    return model

def save_model(model, filename='model1.pkl'):
    pickle.dump(model, open(filename, 'wb'))

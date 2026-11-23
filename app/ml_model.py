
import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from django.conf import settings


MODELS = {}
MODEL_ACCURACIES = {}
BEST_MODEL = None

MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    'trained_crop_models.joblib'
)


def load_and_train_models():
    global MODELS, MODEL_ACCURACIES, BEST_MODEL

    csv_path = os.path.join(
        settings.BASE_DIR,
        'Crop_recommendation.csv'
    )

    if not os.path.exists(csv_path):
        print("ERROR: Dataset not found!")
        return False

    try:
        df = pd.read_csv(csv_path)

        features = [
            'N', 'P', 'K',
            'temperature', 'humidity',
            'ph', 'rainfall'
        ]

        X = df[features]
        y = df['label']

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        algorithms = {
            'random_forest': RandomForestClassifier(
                n_estimators=100,
                random_state=42
            ),

            'decision_tree': DecisionTreeClassifier(
                random_state=42
            ),

            'naive_bayes': GaussianNB(),

            'svm': SVC(
                probability=True,
                random_state=42
            ),

            'knn': KNeighborsClassifier(
                n_neighbors=5
            )
        }

        MODELS = {}
        MODEL_ACCURACIES = {}

        print("\n========== MODEL TRAINING ==========")

        for name, model in algorithms.items():

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            accuracy = accuracy_score(
                y_test,
                predictions
            ) * 100

            MODELS[name] = model
            MODEL_ACCURACIES[name] = round(accuracy, 2)

            print(f"{name}: {accuracy:.2f}%")

        BEST_MODEL = max(
            MODEL_ACCURACIES,
            key=MODEL_ACCURACIES.get
        )

        # Save all trained models and their accuracy
        joblib.dump(
            {
                'models': MODELS,
                'accuracies': MODEL_ACCURACIES,
                'best_model': BEST_MODEL
            },
            MODEL_PATH
        )

        print("\n========== TRAINING RESULTS ==========")
        print("Best Algorithm:", BEST_MODEL)
        print("Best Accuracy:", MODEL_ACCURACIES[BEST_MODEL], "%")
        print("All models saved successfully!")
        print("Saved at:", MODEL_PATH)

        return True

    except Exception as e:
        print("TRAINING ERROR:", str(e))
        return False


def predict_crop(
    n, p, k, temp, humidity, ph, rainfall,
    algorithm='random_forest'
):

    global MODELS

    if not MODELS:
        # Load previously trained models if available
        if os.path.exists(MODEL_PATH):
            saved_data = joblib.load(MODEL_PATH)
            MODELS.update(saved_data['models'])

        else:
            if not load_and_train_models():
                return "Model training failed"

    model = MODELS.get(
        algorithm,
        MODELS.get('random_forest')
    )

    prediction = model.predict([[
        n, p, k, temp, humidity, ph, rainfall
    ]])

    return prediction[0]
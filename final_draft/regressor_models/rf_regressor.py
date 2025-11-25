from .base_regressor import BaseRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd

class RFRegressor(BaseRegressor):
    def __init__(self, n_estimators=300, random_state=42, threshold=0.0, max_depth=10):
        super().__init__("RandomForest")
        self.model = RandomForestRegressor(n_estimators=n_estimators,
                                           random_state=random_state,
                                           max_depth=max_depth)
        self.threshold = threshold
        self.selected_features = None
        self.importances_ = None

    def fit(self, X_train: pd.DataFrame, y_train: pd.Series):
        # 1. Train initial model
        self.model.fit(X_train, y_train)

        # 2. Compute feature importances
        self.importances_ = pd.Series(self.model.feature_importances_,
                                      index=X_train.columns)

        # 3. Select features above threshold
        self.selected_features = self.importances_[self.importances_ > self.threshold].index.tolist()

        # 4. Retrain using selected features only
        self.model.fit(X_train[self.selected_features], y_train)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X[self.selected_features])

from sklearn.ensemble import RandomForestRegressor
from base_regressor import BaseRegressor

class RFRegressor(BaseRegressor):
    def __init__(self, n_estimators=300, random_state=42):
        super().__init__(name="RandomForest")
        self.model = RandomForestRegressor(
            n_estimators=n_estimators,
            random_state=random_state
        )

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

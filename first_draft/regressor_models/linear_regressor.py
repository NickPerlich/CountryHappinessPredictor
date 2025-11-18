from sklearn.linear_model import LinearRegression
from .base_regressor import BaseRegressor

class LinearRegressor(BaseRegressor):
    def __init__(self):
        super().__init__(name="LinearRegression")
        self.model = LinearRegression()

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)

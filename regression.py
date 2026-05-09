import numpy as np

class SimpleRegression:
    def __init__(self, degree=1):
        self.deg = degree
    
    def fit(self, x, y):
        x, y = np.asarray(x), np.asarray(y)
        A, b = [], []
        for i in range(self.deg+1):
            A.append([np.sum(x**(i+j)) for j in range(self.deg+1)])
            b.append(np.sum((x**i)*y))
        
        self.coeffs = np.linalg.solve(A, b)
    
    def predict(self, x):
        return np.dot(np.transpose([x])**range(self.deg+1), self.coeffs)

class MultipleRegression:
    def fit(self, X, y):
        X, y = np.c_[np.ones(len(X)), X].T, np.asarray(y)
        A, b = [], []
        for i in range(len(X)):
            A.append([np.sum(X[i]*X[j]) for j in range(len(X))])
            b.append(np.sum(X[i]*y))
        
        self.coeffs = np.linalg.solve(A, b)
    
    def predict(self, X):
        return np.dot(X, self.coeffs[1:]) + self.coeffs[0]
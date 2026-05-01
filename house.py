import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = [[800], [1000], [1200], [1500]]
y = [30, 40, 50, 65]
model = LinearRegression().fit(X, y)
pred = model.predict([[1200]])
print("Predicted Price:", pred[0])
plt.scatter(X, y)             
plt.plot(X, model.predict(X))  
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price Prediction")
plt.show()
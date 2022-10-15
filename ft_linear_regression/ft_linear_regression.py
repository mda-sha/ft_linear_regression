import pandas as pd
import numpy as np
from decimal import Decimal
from matplotlib import pyplot as plt
from celluloid import Camera
from sklearn.preprocessing import MinMaxScaler

class linearRegression:
  def __init__(self):
    self.intercept = 0
    self.coef = 0
    self.learningRate = 1
    self.iterations = 1000
    self.x_min = 0
    self.x_max = 0


  def train(self, df):
    self.x_min = min(df.km)
    self.x_max = max(df.km)
    scaler = MinMaxScaler()
    x_scaled = scaler.fit_transform(np.array(df.km).reshape(-1,1))
    Y = x_scaled * self.coef + self.intercept

    fig = plt.figure(figsize=(10,4))
    camera = Camera(fig)
 
    for a in range(self.iterations):
      theta0 = 0
      theta1 = 0

      plt.plot(x_scaled, Y, color = "red")
      plt.xlabel("mileage")
      plt.ylabel("price")
      plt.scatter(x_scaled, df.price)
      camera.snap()

      for i in range(df.shape[0]):
        dif = (x_scaled[i] * self.coef + self.intercept) - df.loc[i]["price"]
        theta0 += dif
        theta1 += dif * x_scaled[i]
      self.intercept -= self.learningRate * theta0 / df.shape[0]
      self.coef -= self.learningRate * theta1 / df.shape[0]
      Y = x_scaled * self.coef + self.intercept

      print(self.intercept, self.coef)

    animation = camera.animate()
    plt.show()
  
  def predict(self, x):
    if self.x_min != 0 and self.x_max != 0:
      x = ((x - self.x_min) / (self.x_max - self.x_min))
    y = x * self.coef + self.intercept
    return y

  def setLearningRate(self, newLR):
    self.learningRate = newLR

  def setIterations(self, newIterations):
    self.iterations = newIterations

  def getIntersept(self):
    return self.intercept

  def getCoef(self):
    return self.coef

  # def getAccuracy(self):



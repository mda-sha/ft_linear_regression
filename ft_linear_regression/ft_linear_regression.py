import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

class linearRegression:
  def __init__(self):
    self.intercept = 0
    self.coef = 0
    self.learningRate = 0.1
    # learningRate = 0.0000000001
    self.iterations = 1000


  def train(self, df):
    X = df.km
    Y = X * self.coef + self.intercept

    fig = plt.figure(figsize=(10,4))
    camera = Camera(fig)
 
    for a in range(self.iterations):
      theta0 = 0
      theta1 = 0

      plt.plot(X, Y, color = "red")
      plt.xlabel("mileage")
      plt.ylabel("price")
      plt.scatter(df.km, df.price)
      camera.snap()

      for i in range(df.shape[0]):
        dif = (X[i] * self.coef + self.intercept) - df.loc[i]["price"]
        theta0 += dif
        theta1 += dif * X[i]
      self.intercept -= self.learningRate * theta0 / df.shape[0]
      self.coef -= self.learningRate * theta1 / df.shape[0]
      Y = X * self.coef + self.intercept

    print(self.intercept, self.coef)
    animation = camera.animate()
    plt.show()
  
  def predict(self, x):
    y = x * self.coef + self.intercept
    print(y)
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



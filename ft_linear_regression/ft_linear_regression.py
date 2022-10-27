import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score

class linearRegression:
  def __init__(self,df):
    self.intercept = 0
    self.coef = 0
    self.learningRate = 1
    self.iterations = 1000
    self.df=df


  def train(self):
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
    x_min = min(self.df.km)
    x_max = max(self.df.km)
    if x_min != 0 and x_max != 0:
      x = ((x - x_min) / (x_max - x_min))
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

  def getAccuracy(self):
    y_predict=[]
    y_true=[]
    for i in range(df.shape[0]):
      y_predict.append(lr.predict(df.km[i]))
      y_true.append(df.price[i])
    return r2_score(y_true,y_predict) 





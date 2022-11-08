# import sys
# from os.path import dirname
# sys.path.append('/Users/rricardo/Library/Python/3.8/lib/python/site-packages')

import pandas as pd
from ft_linear_regression import ft_linear_regression

df = pd.read_csv("data.csv")
lr = ft_linear_regression.linearRegression(df)
# df = pd.DataFrame(data = {"km": [1, 2,3, 4], "price":[20, 25, 30, 35]})
print("Hello to our linear regression test program. Here you can test these functions:\nto test predict function please enter 'predict'\nto test train function enter 'train'\nto get accuracy of model print 'get accuracy'\nAlso you can change learning rate and number of iterations")
while True:
    inp = input().lower()
    if inp == "train":
        lr.train()
    if inp == "predict":
        x = input("Please enter value of mileage you want to get prediction for ")
        try:
            x = int(x)
        except:
            print("Wrong value")
            continue
        print(f'Predicted value is {lr.predict(x)}')
    if inp == "get accuracy":
        print(f"Accuracy of model is {lr.getAccuracy()}")
    if inp == "change learning rate":
        l_rate = input("Please enter new value for learning rate ")
        try:
            l_rate = int(l_rate)
        except:
            print("Wrong value")
            continue
        lr.setLearningRate(l_rate)
        print(f'Learning rate is {l_rate}')
    if inp == "change iterations number":
        it = input("Please enter new iterations number ")
        try:
            it = int(it)
        except:
            print("Wrong value")
            continue
        lr.setIterations(it)
        print(f'Iterations number is {it}')
    if inp == "exit":
        exit(0)

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,confusion_matrix
import matplotlib.pyplot as plt
df=pd.read_csv("/content/drive/MyDrive/Copy of kc_house_data.csv")
print(df.columns)
X=df[['sqft_living']]
Y=df[["price"]]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
lg=LinearRegression()
lg=lg.fit(X_train,Y_train)
Y_predict= lg.predict(X_test)
print("MSE:",mean_squared_error(Y_test,Y_predict))
plt.scatter(X_train,Y_train)
plt.plot(X_test,Y_predict,color="r")
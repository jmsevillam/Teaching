import pandas as pd
import quandl, math,datetime
import numpy as np

from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

import matplotlib.pylab as plt
from matplotlib import style

import pickle

style.use("ggplot")

df=quandl.get("WIKI/GOOGL")

#print(df.head())

df=df[["Adj. Open","Adj. Close","Adj. High","Adj. Low","Adj. Volume"]]

df["HL_PCT"] = (df["Adj. High"]-df["Adj. Close"])/df["Adj. Close"] * 100.0

df["PCT_change"] = (df["Adj. Close"]-df["Adj. Open"])/df["Adj. Open"] * 100.0

df = df[["Adj. Close","HL_PCT","PCT_change","Adj. Volume"]]

# print(df.head())

forecast_col="Adj. Close"

df.fillna(-99999, inplace=True)

forecast_out=int(math.ceil(0.01*len(df)))

#print(forecast_out)

df["label"]=df[forecast_col].shift(-forecast_out)

#print(df.head())
#print(df.tail())
df.dropna(inplace=True)
#print(df.head())
#print(df.tail())


X = np.array(df.drop(["label"],1))
#print(X)

X=preprocessing.scale(X)

y=np.array(df["label"])

#print(np.shape(X),np.shape(y))

X_train,X_test,y_train,y_test=model_selection.train_test_split(X,y,test_size=0.2)

clf=LinearRegression()

clf.fit(X_train,y_train)

accuracy=clf.score(X_test,y_test)

#print(accuracy)

'''
clf=svm.SVR()

clf.fit(X_train,y_train)

accuracy=clf.score(X_test,y_test)

print(accuracy)


clf=svm.SVR(kernel="poly")

clf.fit(X_train,y_train)

accuracy=clf.score(X_test,y_test)

print(accuracy)
'''

clf=LinearRegression(n_jobs=10)

clf.fit(X_train,y_train)

accuracy=clf.score(X_test,y_test)

#print(accuracy)




df=quandl.get("WIKI/GOOGL")
df=df[["Adj. Open","Adj. Close","Adj. High","Adj. Low","Adj. Volume"]]
df["HL_PCT"] = (df["Adj. High"]-df["Adj. Close"])/df["Adj. Close"] * 100.0
df["PCT_change"] = (df["Adj. Close"]-df["Adj. Open"])/df["Adj. Open"] * 100.0
df = df[["Adj. Close","HL_PCT","PCT_change","Adj. Volume"]]
df.fillna(-99999, inplace=True)
df["label"]=df[forecast_col].shift(-forecast_out)


X = np.array(df.drop(["label"],1))

X=preprocessing.scale(X)

X= X[:-forecast_out]
X_lately=X[-forecast_out:]


df.dropna(inplace=True)
y=np.array(df["label"])

#print(np.shape(X),np.shape(y))

X_train,X_test,y_train,y_test=model_selection.train_test_split(X,y,test_size=0.2)

clf=LinearRegression()

clf.fit(X_train,y_train)

accuracy=clf.score(X_test,y_test)

#print(accuracy)


forecast_set=clf.predict(X_lately)

#print(forecast_set,accuracy,forecast_out)

df["Forecast"]=np.nan

last_date=df.iloc[-1].name
last_unix=last_date.timestamp()

one_day=86400

next_unix=last_unix+one_day

for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]= [np.nan for _ in range(len(df.columns)-1)]+ [i]
df["Adj. Close"].plot()
df["Forecast"].plot()
plt.legend(loc=4)
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()




X_train,X_test,y_train,y_test=model_selection.train_test_split(X,y,test_size=0.2)

clf=LinearRegression(n_jobs=-1)
clf.fit(X_train,y_train)

with open ('linearregession.pickle','wb') as f:
    pickle.dump(clf,f)

pickle_in = open('linearregession.pickle','rb')

clf=pickle.load(pickle_in)

accuracy=clf.score(X_test,y_test)

#print(accuracy)


forecast_set=clf.predict(X_lately)

#print(forecast_set,accuracy,forecast_out)

df["Forecast"]=np.nan

last_date=df.iloc[-1].name
last_unix=last_date.timestamp()

one_day=86400

next_unix=last_unix+one_day

for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date]= [np.nan for _ in range(len(df.columns)-1)]+ [i]
df["Adj. Close"].plot()
df["Forecast"].plot()
plt.legend(loc=4)
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

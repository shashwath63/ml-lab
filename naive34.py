import pandas as pd
playTennis = pd.read_csv('diabetes2.csv')
print('Given Dataset is : \n ',playTennis,'\n')
from sklearn.preprocessing import LabelEncoder
Le = LabelEncoder()
playTennis['6'] = Le.fit_transform(playTennis['6'])
playTennis['148'] = Le.fit_transform(playTennis['148'])
playTennis['72'] = Le.fit_transform(playTennis['72'])
playTennis['35'] = Le.fit_transform(playTennis['35'])
playTennis['0'] = Le.fit_transform(playTennis['0'])
playTennis['33.6']=Le.fit_transform(playTennis['33.6'])
playTennis['0.627']=Le.fit_transform(playTennis['0.627'])
playTennis['50']=Le.fit_transform(playTennis['50'])
playTennis['1']=Le.fit_transform(playTennis['1'])
print('The encoded dataset is \n', playTennis)
x = playTennis.drop(['1'],axis = 1)
y = playTennis['1']
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
print('\n x_train :\n',x_train)
print('\n y_train :\n',y_train)
print('\n x_test :\n',x_test)
print('\n y_test"\n',y_test)
classifier = GaussianNB()
classifier.fit(x_train, y_train)
accuracy = accuracy_score(classifier.predict(x_test), y_test)
print('accuracy is :\n',accuracy)
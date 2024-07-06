from collections import Counter
import numpy as np
def euclidean_distance(x1,x2):
                distance= np.sqrt(np.sum((x1-x2)**2))
                return distance

class KNN:
                #initaite with k k level of 3
               def __init__(self,k=3):
                self.k=k
                 #fiting the x,y that used for training
               def fit(self,X,y):
                       self.X_train = X
                       self.Y_train =y
                 #predicting based on fiting from b previous 
               def predict(self,X):
                       predictions = [self._predict(x) for x in X]
                       return predictions
               
               def _predict(self,x):
                       #compute distances
                       distances= [euclidean_distance(x, x_train) for x_train in self.X_train]


                       #get the closest k
                       k_indices=np.argsort(distances)[:self.k]
                       K_nearest_labels=[self.Y_train[i] for i in k_indices]


                       #majority voye
                       most_common=Counter(K_nearest_labels).most_common()
                       return most_common[0][0]
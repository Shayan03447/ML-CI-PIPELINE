from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    data=load_iris()
    X=data.data
    y=data.target
    X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=42)
    model=LogisticRegression()
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    acc=accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {acc}")
    joblib.dump(model, "model.joblib")
    return acc
if __name__=="__main__":
    train_model()

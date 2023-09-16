from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
import json
import random
import json
import random
import numpy as np
import pandas as pd
nl_model = load('./nlm')

intentList = {
    2: 'greeting',
    1: 'goodbye',
    6: 'thanks',
    0: 'about',
    4: 'name',
    3: 'help',
    5: 'prakriti'
}

df = pd.read_csv("./sentences_intent.csv",names = ['Sentences', 'target'])
X_train=df.Sentences

def get_intent(msg_count):
    ans = np.argmax(nl_model.predict(msg_count))
    return intentList.get(ans)

vectorizer = CountVectorizer(min_df=1)
vectorizer.fit(X_train.values)

def get_response(msg):
    msg_list= []
    msg_list.append(msg)
    msg_count = vectorizer.transform(msg_list)
    print(get_intent(msg_count))
    
get_response("thank you")

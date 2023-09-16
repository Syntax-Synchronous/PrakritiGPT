from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
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

with open('intents.json', 'r') as f:
    intents = json.load(f)

df = pd.read_csv("./sentences_intent.csv",names = ['Sentences', 'target'])
X_train=df.Sentences

def get_intent(msg_count):
    ans = np.argmax(nl_model.predict(msg_count,verbose = 0))
    return intentList.get(ans)

vectorizer = CountVectorizer(min_df=1)
vectorizer.fit(X_train.values)
bot_name = "Sam"

def get_response(msg):
    # print(intents)
    # msg_list= []
    # msg_list.append(msg)
    
    msg_count = vectorizer.transform([msg])
    tag = get_intent(msg_count)
    for intent in intents["intent"]:
        if tag == 'prakriti':
            pass
        if tag == intent['tag']:
            ans = random.choice(intent["responses"])
            return(f"{bot_name}: {ans} " )
    
while(True):
    msg = input("You: ")
    if(msg == 'quit'):
        break
    print(get_response(msg))

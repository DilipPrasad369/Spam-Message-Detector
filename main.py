from flask import Flask,render_template,request

# Creating server
app = Flask(__name__)

# Defining all urls

@app.route("/homepage")
def firstpage():
    return render_template("page1.html")

@app.route("/page2link",methods=["POST"])
def secondpage():
    
    import pickle
    file = open("model.pkl",'rb')
    model = pickle.load(file)
    file.close()
    
    file = open("model2.pkl",'rb')
    cv = pickle.load(file)
    file.close()
    
    file = open("model3.pkl",'rb')
    le = pickle.load(file)
    file.close()
    
    message = request.form['message']
    
    message_cv = cv.transform([message])
    
    output = model.predict(message_cv)
    
    output = le.inverse_transform(output)
    
    info=[message,output]
    
    if info[1][0] == 'spam':
        return render_template('page2a.html',data=info)
    else:
        return render_template('page2b.html',data=info)

# Running the server
app.run()
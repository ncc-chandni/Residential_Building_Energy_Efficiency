import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__,template_folder='template')
with open('energy_efficieny_model.pickle', 'rb') as f:
    model = pickle.load(f)
#model = pickle.load(open('energy_efficiency_model.pickle', 'rb'))

#@app.route('/')
#def home():
#   return render_template('home.html')

@app.route('/',methods=["GET","POST"])
def getprediction():
    if request.method == "POST":      
        data1 = request.form['a']
        data2 = request.form['b']
        data3 = request.form['c']
        data4 = request.form['d']
        data5 = request.form['e']
        data6 = request.form['f']
        arr = np.array([[data1, data2, data3, data4, data5, data6]])
        prediction = model.predict(arr)
        return f'Predicted Cooling Load using Desicion Tree Algorithm is : {prediction}'
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)

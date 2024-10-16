from flask import Flask, request, render_template
import pickle
app = Flask(__name__)


with open('fraud_detection_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict_fraud', methods = ['POST'])
def predict_fraud():
    if request.method =='POST':
        type = int(request.form.get('type'))
        amount = float(request.form.get('amount'))
        oldbalanceOrg = float(request.form.get('oldbalanceOrg'))
        newbalanceOrig = float(request.form.get('newbalanceOrig'))

        prediction = model.predict([[type,amount,oldbalanceOrg,newbalanceOrig]])
        return render_template('predict_fraud.html', is_fraud = prediction[0])


if __name__ =='__main__':
    app.run(debug=True)
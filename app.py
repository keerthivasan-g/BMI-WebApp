from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    BMI=''
    if request.method == 'POST' and 'weight' in request.form:
        weight=float(request.form.get('weight'))
        height=int(request.form.get('height'))
        BMI=calcbmi(weight,height)


    return render_template("index.html",
                            BMI=BMI)
def calcbmi(weight,height):
    return round(weight/((height/100)**2),2)



app.run()

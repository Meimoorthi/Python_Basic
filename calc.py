from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index')
def index():
    a=55
    b=33
    sum=a+b
    sub=a-b
    mul=a*b
    div=float(num1/num2)
    return render_template('mathcal.html',**locals())

if __name__ =='__main__':
    app.run(debug=True)

import numpy as np
from statistics import mode
from flask import Flask, request, render_template, jsonify,make_response


app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('index.html')


@app.route('/renderResult',methods=['POST']) #post method is used to send parameters in http request
def renderResult():
    values = request.form.to_dict()
   
    # print(values['Data'])
    lst = list(map(int,values["Data"].split(",")))
    print(lst)
    print(len(lst))
    print(np.mean(lst))
    print(np.median(lst))
    print(mode(lst))
    print(min(lst))
    print(max(lst))
    
    
    return make_response(jsonify({"Size":len(lst),"Mean":np.mean(lst),"Median":np.median(lst),"Mode":mode(lst),"Min":min(lst),"Max":max(lst),
                                    "Secret" : "9FXDZ8"}))
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
# This is a sample Python script
import json


import model as m

#import flask library for build apis
from flask import Flask,request, jsonify
#flask cors handing
from flask_cors import CORS , cross_origin



import pickle

app = Flask(__name__)
#enable cross origin for any ip
CORS(app , resources={r"/":{"origins":"*"}})

#Home Api
@app.route("/")
def main():
    return "hello world"

#First Page
@app.route("/home")
@cross_origin()
def home():
    return "First Page"


@app.route("/setMenu" , methods = ["POST"])
@cross_origin()
def model():

    if request.data:
        m.set_menu(request.json["vegi_menu"],request.json["stew_menu"],request.json["meat_menu"])
        m.list_mostSuitable_couple()
        return "success"
        #return request.data

    return "Error no body"

@app.route("/getSuitableCoupleList" , methods = ["GET"])
@cross_origin()
def model2():

    print(m.suitable_couples)
    return {
        "suitableCouples":m.suitable_couples
    }

@app.route("/suitabilityOfCouples" , methods = ["GET"])
@cross_origin()
def model3():

    id1 = request.args.get('id1')
    print('id1 ' + id1)
    id2 = request.args.get('id2')
    print('id2 ' + id2)

    return {
       "percentage": m.suitability_of_couple(int(id1) , int(id2))
    }

@app.route("/stewSuitability" , methods = ["GET"])
@cross_origin()
def model4():
    id1 = request.args.get('id1')
    print('id1 ' + id1)
    id2 = request.args.get('id2')
    print('id2 ' + id2)

    return {
        "percentage": m.stew_suitability(int(id1) , int(id2))
    }


@app.route("/meatSuitability" , methods = ["GET"])
@cross_origin()
def model5():
    id1 = request.args.get('id1')
    print('id1 ' + id1)
    id2 = request.args.get('id2')
    print('id2 ' + id2)
    id3 = request.args.get('id3')
    print('id3 ' + id3)
    return {
        "percentage": m.meet_suitability(int(id1),int(id2),int(id3))
    }

@app.route("/finalSuitability" , methods = ["POST"])
@cross_origin()
def model6():
    #get from body
    if request.data:
        return {
            "percentage":m.final_suitability(request.json["id_list"])
        }

    else:
        return "Error no body"

@app.route("/getMenus" , methods = ["Get"])
@cross_origin()
def model7():

    return {
        "vege menu": m.vege_menu,
        "stew menu":m.stew_menu,
        "meat menu":m.meat_menu
    }






if __name__ == '__main__':
    app.debug = True
    #init api port and ip address of the server
    app.run(host='localhost',port=5000)
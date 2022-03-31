"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime


api = Blueprint('api', __name__)

#esta funcion es la que me crea el token
@api.route('/token', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    print("@@@@@@@@@@@@@@@@@@ llega aqui")
    print(email)
    print(password)
    user = User.query.filter_by(email=email, password=password).first()
    if not user:
        return jsonify({"message":"El usuario no fue encontrado",
        "color": "danger"}), 402
    
    token = create_access_token(identity=user.id)

    data_response = {
        "status": True,
        "token": token,
        "email": user.email,
        "userID": user.id,
        "message": "conseguido!",
        "color": "success"
    }
    return jsonify(data_response), 200


@api.route('/registroUsuarios', methods=['POST'])
def registro():
    email = request.json.get('email')
    password = request.json.get('password')
    name = request.json.get('name')
    lastName = request.json.get('lastName')
    phonenumber = request.json.get('phonenumber')
    license = request.json.get('license')
    adress = request.json.get('adress')
    birthdate = request.json.get('birthdate')
    birthdate = datetime.strptime(birthdate, '%d/%m/%Y') #la fecha hay que escribirla asi: ida/mes/año 2/5/2025


    user = User(email= email , password= password, name= name, lastName= lastName, phonenumber= phonenumber, license= license, adress= adress, birthdate= birthdate, is_active= True)
    db.session.add(user)
    db.session.commit()

    data_response= {
        "email": user.email,
        "password": user.password,
        "name": user.name,
        "lastName": user.lastName,
        "phonenumber": user.phonenumber,
        "license": user.license,
        "adress": user.adress,
        "birthdate": user.birthdate
    }
    return jsonify(data_response), 200

@api.route('/registroMoto', methods=['POST'])
def registroMoto():
    power = request.json.get('email')
    priceday = request.json.get('priceday')
    priceweek = request.json.get('priceweek')
    discount_weekend = request.json.get('discount_weekend')
    discount_week = request.json.get('discount_week')
    comment = request.json.get('comment')
    provincia = request.json.get('provincia')
    ciudad = request.json.get('ciudad')
    direccion = request.json.get('direccion')
    latitud = request.json.get('latitud')
    longitud = request.json.get('longitud')

    moto = Moto(power= power, priceday= priceday, priceweek= priceweek, discount_weekend= discount_weekend, discount_week= discount_week, comment= comment, provincia= provincia, ciudad= ciudad, direccion= direccion, latitud= latitud, longitud= longitud)
    db.session.add(moto)
    db.session.commit()

    data_response= {
        "power": moto.power,
        "priceday": moto.priceday,
        "priceweek": moto.priceweek,
        "discount_weekend": moto.discount_weekend,
        "disocunt_week": moto.discount_week,
        "comment": moto.comment,
        "provincia": moto.provincia,
        "ciudad": moto.ciudad,
        "direccion": moto.direccion,
        "latitud": moto.latitud,
        "longitud": moto.longitud
    }
    return jsonify(data_response), 200




@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
from flask import Flask
from flask_cors import CORS
from routes import *

app = Flask(__name__)
CORS(app)

# firebase = firebase.FirebaseApplication("https://interviews-650d1.firebaseio.com/", None)

app.register_blueprint(routes)

# @app.route('/get_cars', methods=['GET'])
# def get_cars():
#     try:
#         result = firebase.get('interviews-650d1/Car', '')
#         cars = []
#         if result:
#             cars_keys = list(result.keys())
#             cars_values = list(result.values())
#             for car_index in range(len(result)):
#                 car_obj = cars_values[car_index]
#                 car_obj['_id'] = cars_keys[car_index]
#                 cars.append(car_obj)
#         return jsonify(cars)
#     except Exception as e:
#         raise GetAllCarsException()
#
#
# @app.route('/get_car/<string:_id>', methods=['GET'])
# def get_car(_id):
#     try:
#         result = firebase.get('interviews-650d1/Car', _id)
#         return result
#     except Exception as e:
#         raise GetCarException(_id)
#
#
# @app.route('/insert_car', methods=['POST'])
# def insert_car():
#     data = request.json
#     data['time_created'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     try:
#         result = firebase.post('interviews-650d1/Car', data)
#         return result
#     except Exception as e:
#         raise InsertCarException(data)
#
#
# @app.route('/edit_car/<string:_id>', methods=['PUT'])
# def edit_car(_id):
#     data = request.json
#     try:
#         result = firebase.put('interviews-650d1/Car/', _id, data)
#         return result
#     except Exception as e:
#         raise EditCarException(_id, data)
#
#
# @app.route('/delete_car/<string:_id>', methods=['DELETE'])
# def delete_car(_id):
#     try:
#         result = firebase.delete('interviews-650d1/Car/', _id)
#         return result
#     except Exception as e:
#         raise DeleteCarException(_id)


if __name__ == "__main__":
    app.run(debug=True, port=80)

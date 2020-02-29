from flask import request, jsonify, make_response, Blueprint
from firebase_manager import *
from errors import *
from datetime import datetime

routes = Blueprint('routes', __name__)


@routes.route('/get_cars', methods=['GET'])
def get_cars():
    try:
        result = get_all()
        cars = []
        if result:
            cars_keys = list(result.keys())
            cars_values = list(result.values())
            for car_index in range(len(result)):
                car_obj = cars_values[car_index]
                car_obj['_id'] = cars_keys[car_index]
                cars.append(car_obj)
        return make_response(jsonify(cars), 200)
    except Exception as e:
        raise GetAllCarsException()


@routes.route('/get_car/<string:_id>', methods=['GET'])
def get_car(_id):
    try:
        result = get(_id)
        result[_id] = _id
        return make_response(result, 200)
    except Exception as e:
        raise GetCarException(_id)


@routes.route('/insert_car', methods=['POST'])
def insert_car():
    data = request.json
    data['time_created'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        result = insert(data)
        return make_response(result, 200)
    except Exception as e:
        raise InsertCarException(data)


@routes.route('/edit_car/<string:_id>', methods=['PUT'])
def edit_car(_id):
    data = request.json
    data['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        result = edit(_id, data)
        result[_id] = _id
        return make_response(result, 200)
    except Exception as e:
        raise EditCarException(_id, data)


@routes.route('/delete_car/<string:_id>', methods=['DELETE'])
def delete_car(_id):
    try:
        result = delete(_id)
        return make_response('Car deleted', 200)
    except Exception as e:
        raise DeleteCarException(_id)

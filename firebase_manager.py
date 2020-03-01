from firebase import firebase

firebase = firebase.FirebaseApplication("https://interviews-650d1.firebaseio.com/", None)


def get_all():
    result = firebase.get('interviews-650d1/Car', '')
    return result


def get(_id):
    result = firebase.get('interviews-650d1/Car', _id)
    return result


def insert(data):
    result = firebase.post('interviews-650d1/Car', data)
    return result


def edit(_id, data):
    car = get(_id)
    data['time_created'] = car['time_created']
    result = firebase.put('interviews-650d1/Car', _id, data)
    return result


def delete(_id):
    result = firebase.delete('interviews-650d1/Car/', _id)
    return result

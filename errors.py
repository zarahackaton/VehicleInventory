class GetAllCarsException(Exception):
    def __init__(self):
        self.message = 'Error retrieving all cars'


class GetCarException(Exception):
    def __init__(self, _id):
        self.message = 'Error retrieving a specific car. ID: {0}'.format(_id)


class InsertCarException(Exception):
    def __init__(self, data):
        self.message = 'Error inserting a new car to inventory. Data: {0}'.format(data)


class EditCarException(Exception):
    def __init__(self, _id, data):
        self.message = 'Error editing a specific car. ID: {0}, Data: {1}'.format(_id, data)


class DeleteCarException(Exception):
    def __init__(self, _id):
        self.message = 'Error deleting a specific car. ID: {0}'.format(_id)


class Hotel:
    def __init__(self, hotel_id, name, location):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location

    def to_dict(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location
        }

    @staticmethod
    def from_dict(data):
        return Hotel(data["hotel_id"], data["name"], data["location"])

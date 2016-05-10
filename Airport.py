class Airport:
    """Class used to store airport information"""
    def __init__(self, code, name, city, country, latitude, longitude):
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        try:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
        except (ValueError, TypeError):
            print("Error: latitude and longitude should be numeric values")
            self.latitude = 0
            self.longitude = 0

    def __str__(self):
        return "{}: {} Airport, {}, {}" \
               .format(self.code, self.name, self.city, self.country)





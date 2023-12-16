class Sluglim5symbConverter():
    regex = '[-a-zA-Z0-9_]+{5}'
    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
class Contents:
    def __init__(self):
        self.test = 'Hello World'

    def __str__(self):
        return self.test

if __name__=='__main__':
    app = Contents()
    print(app)
class FlaskApplication:
    def __init__(self, app, host, port, debug, **options):
        self.app = app
        self.host = host
        self.port = port
        self.debug = debug
        self.options = options

    def run(self):
        self.app.run(self.host, self.port, debug=self.debug, **self.options)

from faas._http.flask import FlaskApplication


class HTTPServer:
    def __init__(self, app, debug, **options):
        self.app = app
        self.debug = debug
        self.options = options

        if self.debug:
            self.server_class = FlaskApplication
        else:
            try:
                from functions_framework._http.gunicorn import GunicornApplication

                self.server_class = GunicornApplication
            except ImportError as e:
                self.server_class = FlaskApplication

    def run(self, host, port):
        http_server = self.server_class(
            self.app, host, port, self.debug, **self.options
        )
        http_server.run()


def create_server(wsgi_app, debug, **options):
    return HTTPServer(wsgi_app, debug, **options)

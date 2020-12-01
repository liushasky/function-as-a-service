import gunicorn.app.base


class GunicornApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, host, port, debug, **options):
        self.options = {
            "bind": "%s:%s" % (host, port),
            "workers": 1,
            "threads": 8,
            "timeout": 0,
        }
        self.options.update(options)
        self.app = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key, value)

    def load(self):
        return self.app

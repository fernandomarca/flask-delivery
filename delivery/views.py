"""Extensao do flask
    """


def init_app(app):

    @app.route("/")
    def index():
        return "Hello Codeshow"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></form>"

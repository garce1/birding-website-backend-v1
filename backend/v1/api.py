from flask_restplus import Api


class ApiV1(Api):

    def __init__(self, app):
        super().__init__(version='1.0',
                         title='Birding website REST API',
                         description='Backend operations that provide dynamic content to the Birding website',
                         prefix='/api')

        super().init_app(app)

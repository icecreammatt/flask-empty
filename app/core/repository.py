from app.core.models.resource import Resource

class Repository():

    def getResources(self):

        resources = []
        resources.append(Resource('Large app how to', 'https://github.com/mitsuhiko/flask/wiki/Large-app-how-to'))
        resources.append(Resource('Modular Applications with Blueprints', 'http://flask.pocoo.org/docs/blueprints/#blueprints'))
        resources.append(Resource('Flask Mega-Tutorial', 'http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-ajax'))

        return resources
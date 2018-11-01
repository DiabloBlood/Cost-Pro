from flask import Flask
from costpro.model import db, TransHistory
from costpro.utils.loader import get_config



def create_app():

    app = Flask(__name__)

    # setup configs
    conf = get_config()
    app.config.update(conf)

    # setup database
    db.init_app(app)

    # register views
    from costpro.api.api import api
    from costpro.api.assets import assets
    from costpro.views.index import index
    app.register_blueprint(api)
    app.register_blueprint(assets)
    app.register_blueprint(index)

    return app
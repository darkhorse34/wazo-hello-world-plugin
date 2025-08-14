import logging
from .api import bp

log = logging.getLogger(__name__)

class Plugin:
    def load(self, app):
        # 'app' is the Flask app inside wazo-calld
        app.register_blueprint(bp, url_prefix="/api/calld/1.0")
        log.info("[hello-calld] plugin loaded")

    def unload(self, app):
        log.info("[hello-calld] plugin unloaded")

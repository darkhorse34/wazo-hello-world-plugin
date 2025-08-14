import logging
from .api import bp as hello_bp

log = logging.getLogger(__name__)

class Plugin:
    # Some calld versions pass {'app': flask_app, ...}; others pass app directly.
    def load(self, app_or_deps):
        app = app_or_deps.get("app") if isinstance(app_or_deps, dict) else app_or_deps
        app.register_blueprint(hello_bp, url_prefix="/api/calld/1.0")
        log.info("[hello-calld] plugin loaded")

    def unload(self, app_or_deps):
        log.info("[hello-calld] plugin unloaded")

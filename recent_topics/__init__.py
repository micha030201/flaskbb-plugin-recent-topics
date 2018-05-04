# -*- coding: utf-8 -*-
"""
    recent_topics
    ~~~~~~~~~~~~~~

    A recent_topics Plugin for FlaskBB.

    :copyright: (c) 2018 by Михаил Лебедев.
    :license: BSD License, see LICENSE for more details.
"""
import os

from flaskbb.utils.helpers import render_template

from .views import recent_topics_bp


__version__ = "0.0.1"


# connect the hooks
def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")


def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


def flaskbb_load_blueprints(app):
    app.register_blueprint(recent_topics_bp, url_prefix="/recent_topics")


def flaskbb_tpl_navigation_after():
    return render_template("recent_topics_navlink.html")


SETTINGS = {}

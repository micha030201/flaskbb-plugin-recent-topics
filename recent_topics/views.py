# -*- coding: utf-8 -*-
"""
    recent_topics.views
    ~~~~~~~~~~~~~~~~~~~~

    This module contains the views for the
    recent_topics Plugin.

    :copyright: (c) 2018 by Михаил Лебедев.
    :license: BSD License, see LICENSE for more details.
"""
from flask import Blueprint, request
from flaskbb.utils.helpers import real, render_template
from flask_login import current_user
from flaskbb.extensions import db
from flaskbb.forum.models import Post, Topic, TopicsRead
from flaskbb.utils.settings import flaskbb_config


recent_topics_bp = Blueprint("recent_topics_bp", __name__, template_folder="templates")


@recent_topics_bp.route("/")
def index():
    page = request.args.get('page', 1, type=int)

    per_page = flaskbb_config['TOPICS_PER_PAGE']
    user = real(current_user)

    if user.is_authenticated:
        topics = Topic.query.\
            outerjoin(TopicsRead,
                      db.and_(TopicsRead.topic_id == Topic.id,
                              TopicsRead.user_id == user.id)).\
            outerjoin(Post, Topic.last_post_id == Post.id).\
            add_entity(Post).\
            add_entity(TopicsRead).\
            order_by(Topic.last_updated.desc()).\
            paginate(page, per_page, True)
    else:
        topics = Topic.query.\
            outerjoin(Post, Topic.last_post_id == Post.id).\
            add_entity(Post).\
            order_by(Topic.last_updated.desc()).\
            paginate(page, per_page, True)

        topics.items = [(topic, last_post, None)
                        for topic, last_post, in topics.items]

    return render_template(
        'recent_topics.html',
        active_forum_nav=False,
        topics=topics,
    )

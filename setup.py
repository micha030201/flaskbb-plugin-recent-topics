# -*- coding: utf-8 -*-
"""
    recent_topics
    ~~~~~~~~~~~~~~

    Track unread topics.

    :copyright: (c) 2018 by Михаил Лебедев.
    :license: BSD License, see LICENSE for more details.
"""
import ast
import re
from setuptools import find_packages, setup
from setuptools.command.install import install


with open("recent_topics/__init__.py", "rb") as f:
    version_line = re.search(
        r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
    ).group(1)
    version = str(ast.literal_eval(version_line))


setup(
    name="flaskbb-plugin-recent_topics",
    version=version,
    license="BSD License",
    author="Михаил Лебедев",
    author_email="micha030201@gmail.com",
    description="Track unread topics.",
    long_description=__doc__,
    keywords="flaskbb plugin",
    packages=find_packages("."),
    include_package_data=True,
    package_data={
        "": ["recent_topics/translations/*/*/*.mo",
             "recent_topics/translations/*/*/*.po"]
    },
    zip_safe=False,
    platforms="any",
    entry_points={
        "flaskbb_plugins": [
            "recent_topics = recent_topics"
        ]
    },
    install_requires=[
        "FlaskBB"  # pin to a version to has pluggy integration
    ],
    setup_requires=[
        "Babel",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)

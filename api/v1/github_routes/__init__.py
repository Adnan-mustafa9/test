#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint
from flask_caching import Cache

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1/github")

cache = Cache()

from api.v1.github_routes.github_stats import *

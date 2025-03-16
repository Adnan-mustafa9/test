#!/usr/bin/python3
"""EndPoints for GitHub stats project"""
from api.v1.github_routes import app_views
from flask import abort, jsonify, make_response, request
from models.github_stats import GitHubStats
from api.v1.github_routes import cache

# A route to display a user stats
@app_views.route(
    "/<username>",
    methods=["GET"],
    strict_slashes=False,
    )
@cache.cached(timeout=600)
def get_github_user_stats(username):
    stats = GitHubStats.get_user_stats(username)
    return jsonify(stats)


# A route to desplay repos of a user
@app_views.route(
    "/<username>/repos",
    methods=["GET"],
    strict_slashes=False,
    )
@cache.cached(timeout=600)
def get_github_user_repos(username):
    stats = GitHubStats.get_user_repos(username)
    return jsonify(stats)


# A route to display all languages that a user has used across all repos
@app_views.route(
    "/<username>/languages",
    methods=["GET"],
    strict_slashes=False,
    )
@cache.cached(timeout=600)
def get_github_user_languages(username):
    stats = GitHubStats.get_language_breakdown(username)
    return jsonify(stats)

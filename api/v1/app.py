#!/usr/bin/python3
"""app.py to connect to API and serve the UI"""
import os
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from api.v1.github_routes import app_views, cache
from github_stats import GitHubStats  # استخدم الملف الموجود في جذر المشروع

app = Flask(__name__)
app.config["CACHE_TYPE"] = "redis"
app.config["CACHE_REDIS_HOST"] = "localhost"
app.config["CACHE_REDIS_PORT"] = 6379
cache.init_app(app)
app.register_blueprint(app_views)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

# مسار الواجهة لعرض النموذج والتقرير
@app.route("/", methods=["GET", "POST"])
def index():
    stats = None
    if request.method == "POST":
        username = request.form.get("github_username", "").strip()
        if username:
            # جلب بيانات المستخدم باستخدام GitHubStats
            stats = GitHubStats.get_user_stats(username)
            # إضافة اسم المستخدم لعرضه في البطاقة
            stats["username"] = username
    return render_template("index.html", stats=stats)

@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    host = os.getenv('GHSW_API_HOST', '0.0.0.0')
    port = int(os.getenv('GHSW_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True, debug=True)

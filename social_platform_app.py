from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# 1. Custom User Profile Data
user_profile = {
    "username": "CodeExplorer",
    "bio": "Sharing my journey through clean skincare and premium cosmetics.",
    "followers": 142
}

# In-memory database to hold user posts
feed_posts = [
    {"author": "AuraBeauty", "text": "Just tried the new radiant orange serum. The glow is real! ✨"},
    {"author": "SkincareDaily", "text": "Reminder: Never skip your evening hydration routine. 🧴"}
]

# 2. Complete Frontend App Layout (HTML/CSS)
SOCIAL_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CosmoSpace- Community Platform</title>
    <style>
        body { font-family: system-ui, sans-serif; margin: 15px; background-color: #fcf6f5; color: #2d2d2d; }
        .profile-card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; }
        .stat { display: inline-block; margin: 10px 20px; font-weight: bold; }
        .post-input { width: 90%; padding: 10px; margin: 15px 0; border: 1px solid #ccc; border-radius: 6px; }
        .btn { background-color: #7b2cbf; color: white; border: none; padding: 10px 15px; border-radius: 6px; cursor: pointer; }
        .feed-container { margin-top: 25px; }
        .post-card { background: #fff; padding: 12px; margin: 10px 0; border-radius: 8px; border-left: 5px solid #7b2cbf; }
    </style>
</head>
<body>

    <div class="profile-card">
        <h2>👤 @{{ profile.username }}</h2>
        <p><em>{{ profile.bio }}</em></p>
        <div class="stat">Followers: {{ profile.followers }}</div>
        <div class="stat">Posts: {{ posts|length }}</div>
    </div>

    <div class="profile-card" style="margin-top: 15px; text-align: left;">
        <h3>Create New Post</h3>
        <form action="/publish" method="POST">
            <input type="text" name="post_content" class="post-input" placeholder="What's on your mind today?" required>
            <br>
            <button type="submit" class="btn">Publish Post</button>
        </form>
    </div>

    <div class="feed-container">
        <h3>Community Activity Feed</h3>
        {% for post in posts %}
        <div class="post-card">
            <strong>@{{ post.author }}</strong>
            <p>{{ post.text }}</p>
        </div>
        {% endfor %}
    </div>

</body>
</html>
"""

# 3. Routing Logic
@app.route('/')
def timeline():
    return render_template_string(SOCIAL_HTML, profile=user_profile, posts=feed_posts)

@app.route('/publish', methods=['POST'])
def publish():
    new_text = request.form.get('post_content')
    if new_text:
        # Add the post to the top of our feed list
        feed_posts.insert(0, {"author": user_profile["username"], "text": new_text})
    return redirect(url_for('timeline'))

if __name__ == '__main__':
    # Run the server on a unique port to avoid conflicts
    app.run(debug=True, port=8080)

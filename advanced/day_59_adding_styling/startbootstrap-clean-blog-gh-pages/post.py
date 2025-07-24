class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

def parse_json_posts(json_posts_list: list) -> list:
    """Modifies a list of JSON posts to a list of class Post posts"""
    posts_list = []
    for post in json_posts_list:
        posts_list.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))

    return posts_list



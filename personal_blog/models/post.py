import json


class Post:
    """
    class Post pra manipulacao do json
    """

    FILE_PATH = "data/posts.json"

    @staticmethod
    def load_posts():
        # carrega os posts do banco de dados
        with open(Post.FILE_PATH, "r") as file:
            return json.load(file)

    @staticmethod
    def edit_post(post_edited, post_id):
        # editar um post especifico por id
        
        posts = Post.get_all()
        for post in posts:
            if post["id"] == post_id:
                post["title"] = post_edited["title"]
                post["date"] = post_edited["date"]
                post["content"] = post_edited["content"]

        # recebe  posts e salva no banco de dados
        with open(Post.FILE_PATH, "w") as file:
            json.dump(posts, file, indent=4)
            
    @staticmethod
    def save_posts(posts):
         # recebe  posts e salva no banco de dados
        with open(Post.FILE_PATH, "w") as file:
            json.dump(posts, file, indent=4)

    @staticmethod
    def get_all():
        # retorna os posts
        return Post.load_posts()

    @staticmethod
    def get_by_id(post_id):
        # selecionar um post por id eo retorna
        posts = Post.load_posts()
        for post in posts:
            if post["id"] == post_id:
                return post
        return None

    @staticmethod
    def create(new_post):
        # cria um post novo
        posts = Post.load_posts()
        new_post["id"] = len(posts) + 1
        posts.append(new_post)
        Post.save_posts(posts)

    @staticmethod
    def delete(post_id):
        # deleta um post por id
        posts = Post.load_posts()
        posts = [post for post in posts if post["id"] != post_id]
        Post.save_posts(posts)

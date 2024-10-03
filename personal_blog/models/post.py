import json


class Post:
    '''
        class Post pra manipulacao do json
    '''

    FILE_PATH = "data/posts.json"

    @staticmethod
    def load_posts():
        # carrega os posts do banco de dados
        with open(Post.FILE_PATH, "r") as file:
            return json.load(file)

    @staticmethod
    def save_posts(posts):
        # recebe  posts e salva no banco de dados
        with open(Post.FILE_PATH, "r") as file:
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

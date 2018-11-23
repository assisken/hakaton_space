from post import Post


class PostFactory:
    @staticmethod
    def create(post: dict) -> Post:
        return Post(
            post_id=post['id'],
            owner_id=post['owner_id'],
            date=post['date'],
            text=post['text'],
        )

from dataclasses import dataclass


@dataclass
class Post:
    post_id: int
    owner_id: int
    date: int
    text: str

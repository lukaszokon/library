from dataclasses import dataclass
import datetime


@dataclass
class Book:
    id: int
    title: str
    author: str
    genre: str
    published: datetime
    status: str = 'Available'


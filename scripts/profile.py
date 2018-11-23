from dataclasses import dataclass
from typing import Optional, List
from enum import Enum, unique, auto


@unique
class Sex(Enum):
    NOT_SPECIFIED = 0
    FEMALE = 1
    MALE = 2


@unique
class Political(Enum):
    Communist = auto()
    Socialist = auto()
    Moderate = auto()
    Liberal = auto()
    Conservative = auto()
    Monarchist = auto()
    Ultraconservative = auto()
    Apathetic = auto()
    Libertian = auto()


@unique
class PeopleMain(Enum):
    intellect_and_creativity = auto()
    kindness_and_honesty = auto()
    health_and_beauty = auto()
    wealth_and_power = auto()
    courage_and_persistance = auto()
    humor_and_love = auto()


@unique
class LifeMain(Enum):
    family_and_children = auto()
    career_and_money = auto()
    entertainment_and_leisure = auto()
    science_and_research = auto()
    improving_the_world = auto()
    personal_development = auto()
    beauty_and_art = auto()
    fame_and_influence = auto()


@unique
class Gradation(Enum):
    very_negative = auto()
    negative = auto()
    neutral = auto()
    compromisable = auto()
    positive = auto()


@dataclass
class Profile:
    vk_id: int
    first_name: str
    last_name: str
    is_closed: bool
    can_access_closed: bool
    sex: Sex
    photo: str

    deactivated: Optional[str]

    # education
    university: Optional[int]
    university_name: Optional[str]
    faculty: Optional[int]
    faculty_name: Optional[str]
    graduation: Optional[int]

    # personal
    political: Optional[Political]
    langs: Optional[List[str]]
    religion: Optional[str]
    inspired_by: Optional[str]
    people_main: Optional[PeopleMain]
    life_main: Optional[LifeMain]
    smoking: Optional[Gradation]
    alcohol: Optional[Gradation]

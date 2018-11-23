import json
import re
from urllib.parse import urlencode

from requests import get, Response

USER = 'https://vk.com/i_am_tkachyov'
API_URL = 'https://api.vk.com/method'
TOKEN = 'c9f6eae8c9f6eae8c9f6eae828c991c036cc9f6c9f6eae8920e88bd86b6d1234d5fbff4'
VERSION = 5.92


def make_queue(method_name: str, parameters: dict) -> Response:
    parameters_query = urlencode(parameters)
    resp = get(f'{API_URL}/{method_name}?{parameters_query}&v={VERSION}&access_token={TOKEN}')
    return resp


def get_short_name(url: str) -> str:
    regex = re.compile('(https?://vk\.com/)(\w+)')
    match = regex.match(url)
    return match.group(2)


def start():
    user = get_short_name(USER)
    resp_raw = make_queue('users.get', {
        'user_ids': user,
        'fields': ','.join([
            'photo_200_orig', 'city', 'verified', 'sex', 'education', 'personal', 'activities', 'interests'
        ])
    })
    resp = json.loads(resp_raw.content)

    profile_json = resp.get('response', None)[0]
    print(profile_json)
    profile = ProfileFactory.create(profile_json)
    print(profile)

    resp_raw = make_queue('wall.get', {
        'owner_id': profile.vk_id,
        'count': 100,
        'offset': 0,
        'filter': 'owner',

    })
    resp = json.loads(resp_raw.content)
    print(resp)
    posts = [PostFactory.create(post) for post in resp['response']['items']]
    print(posts)

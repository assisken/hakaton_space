import json

from django.shortcuts import render

from scripts.profile_factory import ProfileFactory
from scripts.start import get_short_name, make_queue, USER


def index(request):
    user = get_short_name(USER)
    resp_raw = make_queue('users.get', {
        'user_ids': user,
        'fields': ','.join([
            'photo_200_orig', 'city', 'verified', 'sex', 'education', 'personal', 'activities', 'interests'
        ])
    })
    resp = json.loads(resp_raw.content)

    profile_json = resp.get('response', None)[0]
    ProfileFactory.create(USER, profile_json)

    return render(request, 'index.html', {

    })

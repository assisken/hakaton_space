from main.models import Profile


class ProfileFactory:
    @staticmethod
    def create(url: str, profile: dict) -> Profile:
        try:
            profile = Profile.objects.filter(url=url)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(
                vk_id=profile['id'],
                first_name=profile['first_name'],
                last_name=profile['last_name'],
                is_closed=profile['is_closed'],
                can_access_closed=profile['can_access_closed'],
                sex=profile['sex'],
                photo=profile['photo_200_orig'],

                deactivated=profile.get('deactivated', None),

                # education
                university=profile.get('university', None),
                university_name=profile.get('university_name', None),
                faculty=profile.get('faculty', None),
                faculty_name=profile.get('faculty_name', None),
                graduation=profile.get('graduation', None),

                # personal
                political=profile.get('political', None),
                religion=profile.get('religion', None),
                inspired_by=profile.get('inspired_by', None),
                people_main=profile.get('people_main', None),
                life_main=profile.get('life_main', None),
                smoking=profile.get('smoking', None),
                alcohol=profile.get('alcohol', None),
                url=url
            )
        return profile

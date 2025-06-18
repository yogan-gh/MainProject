from django.contrib.auth.decorators import user_passes_test

def in_group(*group_names):
    def check(user):
        return user.groups.filter(name__in=group_names).exists()
    return user_passes_test(check)
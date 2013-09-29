from django_facebook.api import FacebookUserConverter, get_facebook_graph


def get_facebook_friends(request):
    open_graph = get_facebook_graph(request)
    converter = FacebookUserConverter(open_graph)
    friends = converter.open_facebook.fql(
        u'SELECT uid, name, birthday, sex FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())')
    return friends
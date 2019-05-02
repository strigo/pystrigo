def split_kv(pair):
    """Return tuple for key=value.
    """
    key_value = pair.split('=', 1)
    return key_value[0], key_value[1]


def join_url(base, *args):
    if len(args) == 2:
        return '{}/{}'.format(base.format(args[0]), args[1])
    if '{}' in base:
        return base.format(args[0])
    if len(args) == 1:
        return '{}/{}'.format(base, args[0])
    return base

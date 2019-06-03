def split_kv(pair):
    """Return tuple for key=value.
    """
    key_value = pair.split('=', 1)
    return key_value[0], key_value[1]


def join_url(base, *args, **kwargs):
    """Returns the URL to query.
    """
    # Covers cases where `base` has named arguments (e.g. /events/{event_id}/workspaces),
    # And the case where there are no arguments (e.g. /events).
    formatted_url = base.format(**kwargs)
    if args:
        # This covers the case where we would like to add a parameter to the `base` after
        # Formatting by named arguments has taken place.
        # e.g. /events/EVENT_ID, since the base is really /events, and we need to add
        # EVENT_ID to it somehow.
        formatted_url = '{}/{}'.format(formatted_url, *args)
    return formatted_url

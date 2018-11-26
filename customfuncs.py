def validate(first, last, school):
    """A simple validation function."""
    messages = []

    if len(first) < 1 or len(first) > 50:
        messages.append('First name must be between 1-50 chars.')
    if len(last) < 1 or len(last) > 50:
        messages.append('Last name must be between 1-50 chars.')
    if len(school) < 1 or len(school) > 50:
        messages.append('School must be between 1-50 chars.')

    return messages

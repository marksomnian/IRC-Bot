try:
    import err
    import config
    import stackexchange
except ImportError:
    sys.exit(err.load_module)

def so(command):
    """
    """
    response = ''

    terms = command.split('!so ') #notice the trailing space

    if 1 == len(terms): #no search term given
        response = 'Usage: !so <search term>'
    else:
        so = stackexchange.Site(stackexchange.StackOverflow, \
                'b2zuVN84_UOdaC3zc8Z5aw')

        qs = so.search(intitle = terms[1].lstrip())

        response = qs[0].title + '\r\n' + qs[0].url

    return str(response)

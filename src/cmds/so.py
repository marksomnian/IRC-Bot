##@file so.py
#@brief !so \<search term\>
#@author paullik
#@ingroup moduleFiles

import stackexchange
import urllib2

def so(components): # !so <search term>
    """Search the Stack Overflow site and returns the first question's title and
    URL

    Depends on Stack Exchange API
    """
    response = ''

    terms = components['arguments'].split('!so ') #notice the trailing space

    if 1 == len(terms): #no search term given
        response = 'Usage: !so <search term>'
    else:
        so = stackexchange.Site(stackexchange.StackOverflow, \
                'b2zuVN84_UOdaC3zc8Z5aw')

        try:
            qs = so.search(intitle = terms[1].lstrip())
        except urllib2.HTTPError, e:
            response = 'The server couldn\'t fulfill the request!'

            if hasattr(e, 'reason'):
                response = response + '\r\nReason: ' + str(e.reason)
            elif hasattr(e, 'code'):
                response = response + '\r\nCode: ' + str(e.code)
        else:

            if 1 <= len(qs):
                response = qs[0].title + '\r\n' + qs[0].url
            else:
                response = 'Not found: ' + terms[1]

    return str(response)

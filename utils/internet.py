import urllib


def conected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except Exception:
        return False

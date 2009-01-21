"""
A modified version of BeautifulSoup that adds a safe_find method which throws exceptions if nothing is found.

>>> html = "<a href='/index'>go to index</a>"
>>> bs = ExceptionalSoup(html)
>>> bs.safe_find(name='a', attrs={'href': '/index'})
<a href="/index">go to index</a>
>>> bs.safe_find(name='b')
Traceback (most recent call last):
    ...
ExceptionalSoupError: expected 1 result but got 0 for safe_find(name=b, attrs={}, recursive=True, text=None, kwargs={})
"""
from BeautifulSoup import BeautifulSoup as _BeautifulSoup
class ExceptionalSoupError(RuntimeError):
    pass
class ExceptionalSoup(_BeautifulSoup):
    def safe_find(self, name=None, attrs={}, recursive=True, text=None, **kwargs):
        result = self.findAll(name, attrs, recursive, text, **kwargs)
        if len(result) != 1:
            raise ExceptionalSoupError, 'expected 1 result but got %s for safe_find(name=%s, attrs=%s, recursive=%s, text=%s, kwargs=%s)' % (len(result), name, attrs, recursive, text, kwargs)
        return result[0]
del _BeautifulSoup
    
    

if __name__ == '__main__':
    import doctest
    print "Running doctest . . ."
    doctest.testmod()

from fom.errors import FluidError
from fom.session import Fluid


class Clipboard(object):
    """
    Get/set/clear a clipboard tag in Fluidinfo.
    """

    _username = 'USERNAME'  # Your Fluidinfo username.
    _password = 'PASSWORD'  # Your Fluidinfo password.
    _tag = _username + '/clipboard'

    def __init__(self):
        self._fdb = Fluid()
        self._fdb.login(self._username, self._password)

    def get(self):
        """
        Return the value of the user's clipboard tag if any, else C{None}.
        """
        try:
            result = self._fdb.values.get('has ' + self._tag, [self._tag])
        except FluidError, e:
            print 'Error:', e.args[0].response
            raise
        else:
            values = result.value['results']['id'].values()
            nValues = len(values)
            if nValues == 1:
                return values[0].values()[0]['value']
            if nValues > 1:
                print >>sys.stderr, (
                    "Oops, %d Fluidinfo objects have a %s tag." %
                    len(values), self._tag)

    def set(self, data):
        """
        Set the value of the user's clipboard. Make sure any old clipboard
        tags are removed before setting the new one. We put the clipboard
        tag onto the object whose about value is the same as the user's
        (it could go anywhere since the clipboard utilities find it with a
        search rather than by looking in any definite place).

        @param data: A C{str} of data to set as the clipboard contents.
        """
        self._clear()
        try:
            result = self._fdb.about[self._username][self._tag].put(data)
        except FluidError, e:
            print 'Error:', e.args[0].response
            raise

    def clear(self):
        """
        Clear the user's clipboard by removing the Fluidinfo tag.
        """
        return self._clear()

    def _clear(self):
        """
        Helper function to clear the user's clipboard by removing the
        Fluidinfo tag.
        """
        try:
            result = self._fdb.values.delete('has ' + self._tag, [self._tag])
        except FluidError, e:
            print 'Error:', e.args[0].response
            raise

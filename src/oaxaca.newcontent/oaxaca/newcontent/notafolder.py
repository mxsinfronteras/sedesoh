from five import grok
from zope import schema
from plone.directives import form

class INotaFolder(form.Schema):
    """A container for notas
    """

# Note that we use the standard tabular view for this type, so there
# is no specific view here

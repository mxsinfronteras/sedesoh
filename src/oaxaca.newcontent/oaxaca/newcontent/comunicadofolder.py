from five import grok
from zope import schema
from plone.directives import form

class IComunicadoFolder(form.Schema):
    """A container for comunicados
    """

# Note that we use the standard tabular view for this type, so there
# is no specific view here

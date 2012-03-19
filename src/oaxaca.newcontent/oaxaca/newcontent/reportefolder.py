from five import grok
from zope import schema
from plone.directives import form

class IReporteFolder(form.Schema):
    """A container for reportes
    """

# Note that we use the standard tabular view for this type, so there
# is no specific view here

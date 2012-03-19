from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from zope.configuration import xmlconfig

class OaxacaNewcontent(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import oaxaca.newcontent
        xmlconfig.file('configure.zcml', oaxaca.newcontent, context=configurationContext)
    
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'oaxaca.newcontent:default')

OAXACA_NEWCONTENT_FIXTURE = OaxacaNewcontent()
OAXACA_NEWCONTENT_INTEGRATION_TESTING = IntegrationTesting(bases=(OAXACA_NEWCONTENT_FIXTURE,), name="OaxacaNewcontent:Integration")

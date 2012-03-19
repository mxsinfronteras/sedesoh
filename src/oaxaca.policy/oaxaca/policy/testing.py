from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig

class OaxacaPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import oaxaca.policy
        xmlconfig.file('configure.zcml', oaxaca.policy, context=configurationContext)
        
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'oaxaca.policy:default')

OAXACA_POLICY_FIXTURE = OaxacaPolicy()
OAXACA_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(OAXACA_POLICY_FIXTURE,), name="Oaxaca:Integration")

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class TdfsiteaccountrequestLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import tdf.siteaccountrequest
        xmlconfig.file(
            'configure.zcml',
            tdf.siteaccountrequest,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tdf.siteaccountrequest:default')

TDF_SITEACCOUNTREQUEST_FIXTURE = TdfsiteaccountrequestLayer()
TDF_SITEACCOUNTREQUEST_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TDF_SITEACCOUNTREQUEST_FIXTURE,),
    name="TdfsiteaccountrequestLayer:Integration"
)
TDF_SITEACCOUNTREQUEST_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TDF_SITEACCOUNTREQUEST_FIXTURE, z2.ZSERVER_FIXTURE),
    name="TdfsiteaccountrequestLayer:Functional"
)

from  tdf.siteaccountrequest.testing import TDF_SITEACCOUNTREQUEST_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=TDF_SITEACCOUNTREQUEST_FUNCTIONAL_TESTING)
    ])
    return suite
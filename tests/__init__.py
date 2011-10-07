import unittest

from payex.pxorder import PxOrderInitialize7Handler, PxOrderCompleteHandler
from payex.service import Payex
from payex.utils import XmlDictConfig

# Insert your keys here to test integration
MERCHANT_NUMBER = ''
ENCRYPTION_KEY = ''


class TestService(unittest.TestCase):
    """
    Test initialization of service.
    """
    
    def testServiceSetup(self):
        
        service = Payex(merchant_number='123', encryption_key='secret-string')
        
        # Check default values and setting of kwargs
        self.assertEquals(service.accountNumber, '123')
        self.assertEquals(service.encryption_key, 'secret-string')
        self.assertFalse(service.production)
        
        # Check that handlers are present
        self.assertTrue(isinstance(service.initialize, PxOrderInitialize7Handler))
        self.assertTrue(isinstance(service.complete, PxOrderCompleteHandler))

class TestIntegration(unittest.TestCase):
    """
    Test the initialize7 method.
    """
    
    def testPayment(self):
        
        # Needs credentials to test
        if MERCHANT_NUMBER == '' or ENCRYPTION_KEY == '':
            return
        
        service = Payex(merchant_number=MERCHANT_NUMBER, encryption_key=ENCRYPTION_KEY, production=False)
        
        # Initialize a payment
        response = service.initialize(purchaseOperation='AUTHORIZATION', price='5000', currency='NOK', vat='2500', orderID='test1', productNumber='123', description=u'This is a test.', clientIPAddress='127.0.0.1', clientIdentifier='USERAGENT=test&username=testuser', additionalValues='PAYMENTMENU=TRUE', returnUrl='http://example.org/return', view='PX', cancelUrl='http://example.org/cancel')
        
        # Check the response
        self.assertEquals(type(response), XmlDictConfig)
        self.assertTrue('orderRef' in response)
        self.assertEquals(response['status']['errorCode'], 'OK')
        self.assertTrue(response['redirectUrl'].startswith('https://test-account.payex.com/MiscUI/PxMenu.aspx'))
        
        # Complete the order (even if it's not completed by user)
        response = service.complete(orderRef=response['orderRef'])
        
        self.assertEquals(type(response), XmlDictConfig)
        self.assertEquals(response['status']['errorCode'], 'Order_OrderProcessing')


if __name__ == "__main__":
    unittest.main()
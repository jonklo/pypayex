from suds.client import Client
from payex.handlers import BaseHandler

class PxAgreementHandler(BaseHandler):
    """
    Base handler for PxOrder methods.
    """

    def __call__(self, *args, **kwargs):

        # Set the parameters on object
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

        # Which WDSL URL to use
        if self._service.production:
            self._wdsl_url = 'https://external.payex.com/pxagreement/pxagreement.asmx?WSDL'
        else:
            self._wdsl_url = 'https://test-external.payex.com/pxagreement/pxagreement.asmx?WSDL'

        # Initialize the WDSL schema and set endpoint
        self._client = Client(self._wdsl_url)

###################
# METHOD HANDLERS #
###################

class PxCreateAgreement3Handler(PxAgreementHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxagreement/createagreement3/
    """

    field_order = [
        'accountNumber',
        'merchantRef',
        'description',
        'purchaseOperation',
        'maxAmount',
        'notifyUrl',
        'startDate',
        'stopDate',
    ]

    def __call__(self, *args, **kwargs):

        super(PxCreateAgreement3Handler, self).__call__(*args, **kwargs)

        # Set SOAP endpoint and send request
        self._endpoint = self._client.service.CreateAgreement3

        return self._send_request()

class PxDeleteAgreementHandler(PxAgreementHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxagreement/deleteagreement/
    """

    field_order = [
        'accountNumber',
        'agreementRef',
    ]

    def __call__(self, *args, **kwargs):

        super(PxDeleteAgreementHandler, self).__call__(*args, **kwargs)

        # Set SOAP endpoint and send request
        self._endpoint = self._client.service.DeleteAgreement

        return self._send_request()

class PxAgreementCheckHandler(PxAgreementHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxagreement/agreementcheck/
    """
    
    field_order = [
        'accountNumber',
        'agreementRef',
    ]
    
    def __call__(self, *args, **kwargs):

        super(PxAgreementCheckHandler, self).__call__(*args, **kwargs)

        # Set SOAP endpoint and send request
        self._endpoint = self._client.service.AgreementCheck

        return self._send_request()

class PxAutoPay2Handler(PxAgreementHandler):
    """
    Reference:
    http://www.payexpim.com/technical-reference/pxagreement/autopay2/
    """

    field_order = [
        'accountNumber',
        'agreementRef',
        'price',
        'productNumber',
        'description',
        'orderId',
        'purchaseOperation',
    ]

    def __call__(self, *args, **kwargs):

        super(PxAutoPay2Handler, self).__call__(*args, **kwargs)

        # Set SOAP endpoint and send request
        self._endpoint = self._client.service.AutoPay2

        return self._send_request()

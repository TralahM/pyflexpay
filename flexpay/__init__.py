"""FlexiPay API Client.


.. note::
    The IP address, PORT and Authorization Token are to be provided by
    FlexPay.

"""
import typing
import requests


class API:
    """The API Client.

    :ip: The remote ip address of the FlexPay gateway server
    :port: The remote port of the FlexPay gateway server
    :auth_token: The Bearer authorization token issued by FlexPay

    **Methods.**

    """

    def __init__(
        self,
        remote_ip: str,
        remote_port: typing.Union[int, str],
        authorization_token: str,
    ):
        """Create the api client to this remote ip and port."""
        self.ip = remote_ip
        self.port = remote_port
        self.auth_token = authorization_token

    def _get_url(self, endpoint):
        """Returrn full remote url for the endpoint begining with slash."""
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        return f"https://{self.ip}:{self.port}/api/rest/v1{endpoint}"

    def _get_headers(self):
        """Return the Authorization header dict used in all requests."""
        return {
            "Authorization": f"Bearer {self.auth_token}",
        }

    def check_transaction(self, orderNumber: str):
        """Check the status of a previously sent payment request.

        :param orderNumber: FlexPay internal reference for the transaction.
        :type orderNumber:  str

        :returns: a dict object with details.
        :rtype:  dict

        **Response Parameters**

        :Code: code to indicate the status of the request
            >> ``0`` if correctly received ``1`` if not correctly received.

        :Message: description of the Response

        :Transaction: Object containing the field below

            :reference: Your internal reference of the transaction.

            :orderNumber: FlexPay internal reference for the transaction.

            :status: Code to indicate the status of the transaction.
                >> ``0`` if successful, ``1`` if transaction has failed.

            :amount: the transaction amount sent to gateway.

            :amountCustomer: total amount paid by the customer.

            :currency: The transaction currency.

            :createdAt: The transaction DateTime

        """
        endpoint = f"/check/{orderNumber}"
        url = self._get_url(endpoint)
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        return response.json()

    def payment_service(
        self,
        merchant_code: str,
        your_reference: str,
        customer_phonenumber: str,
        amount: typing.Union[int, str],
        callbackUrl: str,
        transaction_type: typing.Union[int, str] = 1,
        currency: str = "CDF",
    ):
        """Make a payment request to flexpay.

        :param merchant_code: Merchant Code FlexPay
        :type merchant_code: str

        :param transaction_type: The type of transaction
            >> (``1``. mobile money, ``2``. Bank card)
        :type transaction_type: typing.Union[int, str]

        :param your_reference: Your internal reference for the transaction
        :type your_reference: str

        :param customer_phonenumber: Phone number of the customer.
        :type customer_phonenumber: str

        :param amount: The transaction amount.
        :type amount: typing.Union[int, str]

        :param currency: The transaction currency (CDF or USD).
        :type currency: str

        :param callbackUrl: The Callback URL where the transaction
            result will be sent.
        :type callbackUrl: str

        :returns: a dict object with details code, message, orderNumber.
        :rtype:  dict

        **Description of Response Parameters**

        :code: code to indicate the status of the request
            ``0`` if correctly received ``1`` if not correctly received.

        :message: A description of the response

        :orderNumber: FlexPay internal reference for the transaction.

        A request is sent to the CallBack URL to provide status of the
        transaction.

        **Description fields of Result.**

        :Code: code to indicate the status of the request
            ``0`` if correctly received ``1`` if not correctly received.

        :Reference: Your internal reference of the transaction

        :Provider_reference: The transaction reference from the mobile money
            operator if the transaction was successful.

        :orderNumber: FlexPay internal reference of the transaction.


        """
        endpoint = "/paymentService"
        url = self._get_url(endpoint)
        headers = self._get_headers()
        data = {
            "merchant": merchant_code,
            "type": transaction_type,
            "reference": your_reference,
            "phone": customer_phonenumber,
            "amount": amount,
            "currency": currency,
            "callbackUrl": callbackUrl,
        }
        response = requests.post(url, headers=headers, data=data)
        return response.json()

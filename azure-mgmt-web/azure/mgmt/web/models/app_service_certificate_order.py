# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class AppServiceCertificateOrder(Resource):
    """SSL certificate purchase order.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Required. Resource Location.
    :type location: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param certificates: State of the Key Vault secret.
    :type certificates: dict[str,
     ~azure.mgmt.web.models.AppServiceCertificate]
    :param distinguished_name: Certificate distinguished name.
    :type distinguished_name: str
    :ivar domain_verification_token: Domain verification token.
    :vartype domain_verification_token: str
    :param validity_in_years: Duration in years (must be between 1 and 3).
     Default value: 1 .
    :type validity_in_years: int
    :param key_size: Certificate key size. Default value: 2048 .
    :type key_size: int
    :param product_type: Required. Certificate product type. Possible values
     include: 'StandardDomainValidatedSsl',
     'StandardDomainValidatedWildCardSsl'
    :type product_type: str or ~azure.mgmt.web.models.CertificateProductType
    :param auto_renew: <code>true</code> if the certificate should be
     automatically renewed when it expires; otherwise, <code>false</code>.
     Default value: True .
    :type auto_renew: bool
    :ivar provisioning_state: Status of certificate order. Possible values
     include: 'Succeeded', 'Failed', 'Canceled', 'InProgress', 'Deleting'
    :vartype provisioning_state: str or
     ~azure.mgmt.web.models.ProvisioningState
    :ivar status: Current order status. Possible values include:
     'Pendingissuance', 'Issued', 'Revoked', 'Canceled', 'Denied',
     'Pendingrevocation', 'PendingRekey', 'Unused', 'Expired', 'NotSubmitted'
    :vartype status: str or ~azure.mgmt.web.models.CertificateOrderStatus
    :ivar signed_certificate: Signed certificate.
    :vartype signed_certificate: ~azure.mgmt.web.models.CertificateDetails
    :param csr: Last CSR that was created for this order.
    :type csr: str
    :ivar intermediate: Intermediate certificate.
    :vartype intermediate: ~azure.mgmt.web.models.CertificateDetails
    :ivar root: Root certificate.
    :vartype root: ~azure.mgmt.web.models.CertificateDetails
    :ivar serial_number: Current serial number of the certificate.
    :vartype serial_number: str
    :ivar last_certificate_issuance_time: Certificate last issuance time.
    :vartype last_certificate_issuance_time: datetime
    :ivar expiration_time: Certificate expiration time.
    :vartype expiration_time: datetime
    :ivar is_private_key_external: <code>true</code> if private key is
     external; otherwise, <code>false</code>.
    :vartype is_private_key_external: bool
    :ivar app_service_certificate_not_renewable_reasons: Reasons why App
     Service Certificate is not renewable at the current moment.
    :vartype app_service_certificate_not_renewable_reasons: list[str]
    :ivar next_auto_renewal_time_stamp: Time stamp when the certificate would
     be auto renewed next
    :vartype next_auto_renewal_time_stamp: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
        'type': {'readonly': True},
        'domain_verification_token': {'readonly': True},
        'validity_in_years': {'maximum': 3, 'minimum': 1},
        'product_type': {'required': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'signed_certificate': {'readonly': True},
        'intermediate': {'readonly': True},
        'root': {'readonly': True},
        'serial_number': {'readonly': True},
        'last_certificate_issuance_time': {'readonly': True},
        'expiration_time': {'readonly': True},
        'is_private_key_external': {'readonly': True},
        'app_service_certificate_not_renewable_reasons': {'readonly': True},
        'next_auto_renewal_time_stamp': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'certificates': {'key': 'properties.certificates', 'type': '{AppServiceCertificate}'},
        'distinguished_name': {'key': 'properties.distinguishedName', 'type': 'str'},
        'domain_verification_token': {'key': 'properties.domainVerificationToken', 'type': 'str'},
        'validity_in_years': {'key': 'properties.validityInYears', 'type': 'int'},
        'key_size': {'key': 'properties.keySize', 'type': 'int'},
        'product_type': {'key': 'properties.productType', 'type': 'CertificateProductType'},
        'auto_renew': {'key': 'properties.autoRenew', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'status': {'key': 'properties.status', 'type': 'CertificateOrderStatus'},
        'signed_certificate': {'key': 'properties.signedCertificate', 'type': 'CertificateDetails'},
        'csr': {'key': 'properties.csr', 'type': 'str'},
        'intermediate': {'key': 'properties.intermediate', 'type': 'CertificateDetails'},
        'root': {'key': 'properties.root', 'type': 'CertificateDetails'},
        'serial_number': {'key': 'properties.serialNumber', 'type': 'str'},
        'last_certificate_issuance_time': {'key': 'properties.lastCertificateIssuanceTime', 'type': 'iso-8601'},
        'expiration_time': {'key': 'properties.expirationTime', 'type': 'iso-8601'},
        'is_private_key_external': {'key': 'properties.isPrivateKeyExternal', 'type': 'bool'},
        'app_service_certificate_not_renewable_reasons': {'key': 'properties.appServiceCertificateNotRenewableReasons', 'type': '[str]'},
        'next_auto_renewal_time_stamp': {'key': 'properties.nextAutoRenewalTimeStamp', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(AppServiceCertificateOrder, self).__init__(**kwargs)
        self.certificates = kwargs.get('certificates', None)
        self.distinguished_name = kwargs.get('distinguished_name', None)
        self.domain_verification_token = None
        self.validity_in_years = kwargs.get('validity_in_years', 1)
        self.key_size = kwargs.get('key_size', 2048)
        self.product_type = kwargs.get('product_type', None)
        self.auto_renew = kwargs.get('auto_renew', True)
        self.provisioning_state = None
        self.status = None
        self.signed_certificate = None
        self.csr = kwargs.get('csr', None)
        self.intermediate = None
        self.root = None
        self.serial_number = None
        self.last_certificate_issuance_time = None
        self.expiration_time = None
        self.is_private_key_external = None
        self.app_service_certificate_not_renewable_reasons = None
        self.next_auto_renewal_time_stamp = None

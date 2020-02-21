from django.conf import settings
INSTALLED_APPS = (

    'payonline',
)


CONFIG = {
    'MERCHANT_ID': None,
    'PRIVATE_SECURITY_KEY': None,
    'PAYONLINE_URL': 'https://secure.payonlinesystem.com/ru/payment/select/',
    'CURRENCY': 'RUB',
}
PAYONLINE_CONFIG = {
    'MERCHANT_ID': '...',
    'PRIVATE_SECURITY_KEY': '...',
}
CONFIG.update(getattr(settings, 'PAYONLINE_CONFIG', {}))

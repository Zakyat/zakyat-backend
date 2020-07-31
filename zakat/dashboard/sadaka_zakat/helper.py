TRANSACTION_TYPES = {
    'sadaka': '0',
    'zakat': '1',
    'direct': '2'
}


def get_amount(query):
    try:
        amount = int(query)
    except:
        amount = -1
    return amount


def get_transaction_type(query):
    try:
        return TRANSACTION_TYPES[query]
    except:
        return '404_transaction_type'

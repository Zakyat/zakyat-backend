import requests
import json
from sberbank.service import BankService
from sberbank.models import Payment, Status

# request = requests.post(
#     'https://3dsec.sberbank.ru/payment/rest/register.do',
#     data={
#         'userName': 'zakyatrt-api',
#         'password': 'zakyatrt',
#         'orderNumber': '1001',
#         'amount': 123000,
#         'returnUrl': 'http://127.0.0.1:8000/payment_done',
#         'failUrl': 'http://127.0.0.1:8000/payment_fail'
#     }
# )
#
#
# print(request.text)

def send_request_for_payment():
    request = requests.post(
        'https://3dsec.sberbank.ru/payment/rest/register.do',
        data={
            'userName': 'zakyatrt-api',
            'password': 'zakyatrt',
            'orderNumber': '1004',
            'amount': 150000,
            'returnUrl': 'http://127.0.0.1:8000/payment_done',
            'failUrl': 'http://127.0.0.1:8000/payment_fail',
            'jsonParams': json.dumps({'Номер сбора': 12,})
        }
    )

    if request.status_code == 200:
        return json.loads(request.text)
    else:
        return 'Не успешно!'


def make_payment():
    respose = send_request_for_payment()
    print(respose)
    # print(respose['errorCode'])
    # print(type(respose))
    pass



def main(request):
    try:
        # Сумма в рублях
        amount = 2000.0

        # Уникальный ID пользователя, используется для привязки карт
        # Если None, пользователь не сможет выбрать ранее привязанную карту
        # или привязать карту в процессе оплаты
        client_id = request.user.id

        svc = BankService('zakyatrt-operator')

        # url - адрес, на который следует перенаправить пользователя для оплаты
        # payment - объект Payment из БД, содержит информацию о платеже
        # description - назначение платежа в веб-форме банка
        # params - произвольные параметры, которые можно привязать к платежу
        payment, url = svc.pay(amount, params={'Номер сбора': 12}, client_id=client_id,
                               description="Оплата заказа №1234")
        print(url)
    except Exception as exc:
        # Что-то пошло не так
        raise



if __name__ == '__main__':
    make_payment()


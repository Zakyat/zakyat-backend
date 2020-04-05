import graphene
from graphene_django.types import DjangoObjectType
from .models import Transaction

class TransactionSchema(DjangoObjectType):
	class Meta:
		model = Transaction

class Query(object):
    transaction = graphene.Field(TransactionSchema, id=graphene.Int())
    transactions = graphene.List(TransactionSchema)

    def resolve_transaction(self, info, **kwargs):
        return Transaction.objects.get(**kwargs)
    def resolve_transactions(self, info, **kwargs):
        return Transaction.objects.all()

from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from .models import User, Employee


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interfaces = (Node,)
        filter_fields = ["user__first_name", "phone_number"]
    # work = graphene.Field()


# class EmployeeNode(DjangoObjectType):
#     class Meta:
#         model = Employee
#         # Allow for some more advanced filtering here
#         interfaces = (Node,)


class Query(object):
    user = Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

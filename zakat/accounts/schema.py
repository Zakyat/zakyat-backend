import graphene
from graphene_django.types import DjangoObjectType
from .models import Work, CashFlow, Document, FamilyMember, User, Employee, DjangoUser

class WorkSchema(DjangoObjectType):
    class Meta:
        model = Work

class CashFlowSchema(DjangoObjectType):
    class Meta:
        model = CashFlow

class DocumentSchema(DjangoObjectType):
    class Meta:
        model = Document

class FamilyMemberSchema(DjangoObjectType):
    class Meta:
        model = FamilyMember
    identification = graphene.Field(DocumentSchema)

class DjangoUserSchema(DjangoObjectType):
    class Meta:
        model = DjangoUser

class UserSchema(DjangoObjectType):
    class Meta:
        model = User
    work = graphene.Field(WorkSchema)
    cash_flow = graphene.List(CashFlowSchema)
    related_documents = graphene.List(DocumentSchema)
    contact_person = graphene.Field(FamilyMemberSchema)
    family_members = graphene.List(FamilyMemberSchema)

class EmployeeSchema(DjangoObjectType):
    class Meta:
        model = Employee

class Query(object):
    user = graphene.Field(UserSchema, id=graphene.Int())
    users = graphene.List(UserSchema)

    employee = graphene.Field(EmployeeSchema, id=graphene.Int())
    employees = graphene.List(EmployeeSchema)

    def resolve_user(self, info, **kwargs):
        return User.objects.get(**kwargs)
    def resolve_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_employee(self, info, **kwargs):
        return Employee.objects.get(**kwargs)
    def resolve_employees(self, info, **kwargs):
        return Employee.objects.all()

import graphene
from django.db.models import Sum
from graphene_django import DjangoObjectType
from .models import User, Transaction


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', )


class UserInput(graphene.InputObjectType):
    name = graphene.String()
    email = graphene.String()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Input:
        input = UserInput(required=True)

    @staticmethod
    def mutate(self, info, input=None):
        user = User(
            name=input.name,
            email=input.email
        )
        user.save()
        return CreateUser(user=user)


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
        fields = ('id', 'total', 'user', )


class TransactionInput(graphene.InputObjectType):
    total = graphene.Int()
    status = graphene.String()
    user_id = graphene.Int()


class CreateTransaction(graphene.Mutation):
    transaction = graphene.Field(TransactionType)

    class Input:
        input = TransactionInput(required=True)

    @staticmethod
    def mutate(self, info, input=None):
        transaction = Transaction(
            total=input.total,
            status=input.status,
            user_id=input.user_id
        )
        transaction.save()
        return CreateTransaction(transaction=transaction)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_transaction = CreateTransaction.Field()


class Query(graphene.ObjectType):

    all_users = graphene.List(UserType)
    all_transactions = graphene.List(TransactionType)
    user_by_id = graphene.Field(UserType, id=graphene.Int())
    user_by_email = graphene.Field(UserType, email=graphene.String())
    balance_by_user_id = graphene.Int(user_id=graphene.Int())


    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_transactions(root, info):
        return Transaction.objects.all()

    def resolve_user_by_id(root, info, id):
        return User.objects.get(id=id)

    def resolve_user_by_email(root, info, email):
        return User.objects.get(email=email)

    def resolve_balance_by_user_id(root, info, user_id):
        deposit_aggr_sum = Transaction.objects.filter(
            user_id=user_id,
            status='deposit'
        ).aggregate(
            sum=Sum('total')
        )
        withdraw_aggr_sum = Transaction.objects.filter(
            user_id=user_id,
            status='withdraw'
        ).aggregate(
            sum=Sum('total')
        )
        deposit_sum = deposit_aggr_sum['sum'] if deposit_aggr_sum['sum'] is not None else 0
        withdraw_sum = withdraw_aggr_sum['sum'] if withdraw_aggr_sum['sum'] is not None else 0

        return deposit_sum-withdraw_sum


schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene
from graphene_django import DjangoObjectType

from .models import Pod


class PodType(DjangoObjectType):
    class Meta:
        model = Pod


class Query(graphene.ObjectType):

    pods = graphene.List(PodType)

    def resolve_pods(self, info, **kwargs):
        return Pod.objects.all()

    def resolve_pod(self, info, **kwargs):
        return Pod.objects.get(id=kwargs.get('id'))


class CreatePod(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    #2
    class Arguments:
        url = graphene.String()
        description = graphene.String()

    #3
    def mutate(self, info, url, description):
        pod = Pod(url=url, description=description)
        pod.save()

        return CreatePod(
            id=pod.id,
            url=pod.url,
            description=pod.description,
        )


#4
class Mutation(graphene.ObjectType):
    create_pod = CreatePod.Field()
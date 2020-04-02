from rest_framework import serializers
from .models import Project, ProjectComment, ScopeOfWork, ContactData, ContactPerson


class ProjectSerializer(serializers.ModelSerializer):
    owner_ID = serializers.ReadOnlyField(source='owner_ID.username')
    scope_of_work = serializers.SerializerMethodField()
    contact_person = serializers.SerializerMethodField()
    project_comment = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_scope_of_work(self, obj):
        qs = obj.scopeofwork_project_ID.all()
        return ScopeOfWorkSerializer(qs, many=True, read_only=True).data

    def get_contact_person(self, obj):
        qs = obj.contactperson_project_ID.all()
        return ContactPersonSerializer(qs, many=True, read_only=True).data

    def get_project_comment(self, obj):
        qs = obj.projectcomment_project_ID.all()
        return ProjectCommentSerializer(qs, many=True, read_only=True).data


class ScopeOfWorkSerializer(serializers.ModelSerializer):
    owner_ID = serializers.ReadOnlyField(source='owner_ID.username')

    class Meta:
        model = ScopeOfWork
        fields = (
            'deleted',
            'id',
            'created',
            'modified',
            'owner_ID',
            'scope',
            'quantity',
            'description',
            'project_ID',
        )


class ContactPersonSerializer(serializers.ModelSerializer):
    owner_ID = serializers.ReadOnlyField(source='owner_ID.username')
    contact_data = serializers.SerializerMethodField()

    class Meta:
        model = ContactPerson
        fields = (
            'deleted',
            'id',
            'created',
            'modified',
            'owner_ID',
            'name',
            'position',
            'project_ID',
            'contact_data',
        )

    def get_contact_data(self, obj):
        qs = obj.contactdata_project_ID.all()
        return ContactDataSerializer(qs, many=True, read_only=True).data


class ContactDataSerializer(serializers.ModelSerializer):
    owner_ID = serializers.ReadOnlyField(source='owner_ID.username')

    class Meta:
        model = ContactData
        fields = (
            'deleted',
            'id',
            'created',
            'modified',
            'owner_ID',
            'value',
            'type',
            'contact_person_ID',
        )


class ProjectCommentSerializer(serializers.ModelSerializer):
    owner_ID = serializers.ReadOnlyField(source='owner_ID.username')

    class Meta:
        model = ProjectComment
        fields = (
            'deleted',
            'id',
            'created',
            'modified',
            'owner_ID',
            'content',
            'project_ID',
        )

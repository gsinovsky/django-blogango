from django.apps import AppConfig


class BlogangoConfig(AppConfig):
    name = 'blogango'
    verbose_name = "Django Blogango"

    def ready(self):
        from .models import Comment, CommentModerator
        from django.contrib.comments.moderation import moderator

        if Comment not in moderator._registry:
            moderator.register(Comment, CommentModerator)

        from south.modelsinspector import add_introspection_rules
        add_introspection_rules([], ["^markupfield\.fields\.MarkupField"])

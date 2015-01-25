from django.apps import AppConfig


class BlogangoConfig(AppConfig):
    name = 'blogango'
    verbose_name = "Django Blogango"

    def ready(self):
        from south.modelsinspector import add_introspection_rules
        add_introspection_rules([], ["^markupfield\.fields\.MarkupField"])

from django.apps import AppConfig


class BlogangoConfig(AppConfig):
    name = 'blogango'
    verbose_name = "Django Blogango"

    def ready(self):
        from south.modelsinspector import add_introspection_rules
        add_introspection_rules([], ["^markupfield\.fields\.MarkupField"])

        # ping_details = {'blogango_details': pingback_blog_handler}
        from pingback import register_pingback, ping_func
        from . import pingback_blog_handler
        from django_xmlrpc import xmlrpcdispatcher

        register_pingback('blogango.views.details', pingback_blog_handler)

        xmlrpcdispatcher.register_function(ping_func, 'pingback.ping')

from django.db import models

class StoredTemplate(models.Model):
    template_id = models.AutoField(primary_key= True, blank= False, null= False)
    name = models.CharField(max_length=100, null= False, blank= False)
    description = models.TextField(max_length= 300, null= True, blank= True)
    content = models.TextField(max_length=1048, null= False, blank= False)

    def render_template(self, context):
        from django.template import engines
        django_engine = engines['django']
        template = django_engine.from_string(self.content)
        rendered_content = template.render(context)
        return rendered_content

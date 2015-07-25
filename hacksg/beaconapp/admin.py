from django.contrib import admin
from .models import NodeType
from .models import Node
from .models import Reading

# Register your models here.

admin.site.register(NodeType)
admin.site.register(Node)
admin.site.register(Reading)

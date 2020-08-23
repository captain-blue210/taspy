import json
from rest_framework.renderers import JSONRenderer

class TaskListJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'tasks': data},ensure_ascii=False)

class TaskJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'task': data},ensure_ascii=False)

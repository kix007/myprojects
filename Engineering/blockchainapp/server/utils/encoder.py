import json
from datetime import datetime


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat(" ")
        else:
            return super().default(self, obj)


def dumps(obj):
    return json.dumps(obj, cls=Encoder)

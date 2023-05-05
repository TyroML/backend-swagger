import os
import sys
import yaml

from fastapi.openapi.utils import get_openapi

sys.path.append(os.path.join(os.path.dirname(__file__), "../app/api"))

from main import app


with open('backend-swagger/swagger.yaml', 'w') as f:
    yaml.dump(get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes
    ), f)

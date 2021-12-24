
from flask import Blueprint
import json
from flask import request
import gmaiApi as gm

# inicializamos el blueprint
apirestgmail = Blueprint('apirestgmail', __name__)


@apirestgmail.route('/app/correo', methods=["GET"])
def enviarmesseg():
    gm.Mandandomesseg(request.args.get('messeg'),
                      request.args.get('nombre'), request.args.get('numero'), request.args.get('correo'))
    return json.dumps({"mensaje": "la peticion fue enviada con exito"})

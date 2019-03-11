#!/usr/bin/python
from flask import Flask
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
##from m09_model_deployment import predict_price

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Predición del Precio de Carros API',
    description='Precio de Carros API')

ns = api.namespace('predict', 
     description='Predición del Precio')
   
parser = api.parser()

parser.add_argument(
    'Año', 
    type=int, 
    required=True, 
    help='Año del modelo: 1997 a 2018', 
    location='args')
parser.add_argument(    
    'Kilometraje', 
    type=int, 
    required=True, 
    help='Kms recorridos: 5 a 2.457.832',
    location='args')
parser.add_argument(  
    'Estado', 
    type=str, 
    required=True, 
    help='2 letras del nombre del estado.',
    location='args')
parser.add_argument(  
    'Modelo', 
    type=str, 
    required=True, 
    help='Referencia del modelo',
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PricingApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
                print('OK')
                ##"result": predict_price(args['Año','Kilometraje','Estado','Modelo'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

from flask import Flask, jsonify, request, abort
from models import setup_db, Plant
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  setup_db(app)
  # Can state specific origins, resources 
  # CORS(app, resources={r"*/api/*" : {origins: '*'}})
  CORS(app)
  # app after request decorator: after request is received 
  # run this method 
  @app.after_request
  def after_request(response):
    # add headers to response 
    # allow content type, authorization
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization') 
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
  # specific endpoints to allow CORS, use decorator @cross_origin
  @app.route('/')
  def hello():
    return jsonify({'message': 'HELLO WORLD'})

  return app



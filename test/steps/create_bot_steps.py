from behave import given, when, then
import requests
import json

@given('que la aplicacion esta en ejecucion en el puerto 8000')
def step_given_app_running(context):
    pass

@when('hago una solicitud POST a "{url}" con el body')
def step_when_make_post_request(context, url):
    headers = {"Content-Type": "application/json"}
    context.response = requests.post(url, data=context.text, headers=headers)
    context.response_data = context.response.json()

@then('deberia recibir una respuesta exitosa de status 200')
def step_then_receive_successful_response(context):
    assert context.response.status_code == 200

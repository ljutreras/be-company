from behave import given, when, then
import requests
import json

@given('que la aplicacion esta en ejecucion')
def step_given_app_running(context):
    pass

@when('hago una peticion POST a "{url}" con el body')
def step_when_make_post_request(context, url):
    headers = {"Content-Type": "application/json"}
    context.response = requests.post(url, data=context.text, headers=headers)
    context.response_data = context.response.json()

@then('recibire una respuesta exitosa de status 200')
def step_then_receive_successful_response(context):
    assert context.response.status_code == 200

@then('contiene la respuesta')
def step_then_response_contains(context):
    expected_data = json.loads(context.text)
    expected_data['data']['id'] = context.response_data['data']['id']
 
    assert context.response_data == expected_data

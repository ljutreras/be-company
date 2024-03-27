from behave import given, when, then
import requests
import json

@given('que la aplicacion se encuentra en ejecucion')
def step_given_app_running(context):
    pass

@when('hago una peticion GET a "{url}"')
def step_when_make_get_request(context, url):
    headers = {"Content-Type": "application/json"}
    context.response = requests.get(url, headers=headers)
    context.response_data = context.response.json()

@then('recibire una respuesta de status 200')
def step_then_receive_successful_response(context):
    assert context.response.status_code == 200

@then('contendra la respuesta')
def step_then_response_contains(context):
    expected_data = json.loads(context.text)
    assert context.response_data == expected_data

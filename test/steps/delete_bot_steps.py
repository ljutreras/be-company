from behave import given, when, then
from behave import use_fixture
import requests
import json

@given('que la aplicación se esta ejecutando')
def step_given_app_running(context):
    pass

@when('hago una petición DELETE a "{url}"')
def step_when_make_delete_request(context, url):
    headers = {"Content-Type": "application/json"}
    context.response = requests.delete(url, headers=headers)

@then('la respuesta tiene que ser {status_code}')
def step_then_response_contains(context, status_code):
    assert context.response.status_code == int(status_code)


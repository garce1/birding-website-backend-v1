from behave import given, when, then


@given('we have at least one gallery record')
def step_impl(context):
    pass


@when('we retrieve the available galleries')
def step_impl(context):  # -- NOTE: number is converted into integer
    pass


@then('the API will return all of them')
def step_impl(context):
    pass

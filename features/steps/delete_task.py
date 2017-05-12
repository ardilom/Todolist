from behave import given, when, then

@given(u'I go to "/tasks" to delete a task')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/tasks')

@when(u'I select the delete button of task "Buy bread and milk and beer, it\'s friday!!!"')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('name').send_keys('Buy bread and milk and beer, it\'s friday!!!')
    br.find_element_by_id('add_submit').click()
    br.find_element_by_id('delete_submit').click()

@then(u'I should no longer be able  to see the task "Buy bread and milk and beer, it\'s friday!!!" on the list')
def step_impl(context):
    br = context.browser
    assert "Buy bread and migit hf feature finish behavelk and beer, it\'s friday!!!" not in br.page_source


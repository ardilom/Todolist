from behave import given, when, then

@given(u'I go to "/tasks" to finish a task')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/tasks')
    
@when(u'I fill select the complete button of task "Buy bread and milk and beer, it\'s friday!!!"')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('name').send_keys('Buy bread and milk and beer, it\'s friday!!!')
    br.find_element_by_id('add_submit').click()
    br.find_element_by_id('complete_submit').click()

@then(u'I should be able to see the task "Buy bread and milk and beer, it\'s friday!!!", as completed.')
def step_impl(context):
    br = context.browser
    assert "completed" in br.page_source
    #TODO mejorar el assert (verificar que la clase de la task tenga completed)
    # assert "Buy bread and milk and beer, it\'s friday!!! - completed" in br.page_source
    
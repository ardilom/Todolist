from behave import given, when, then
from selenium import webdriver

@given(u'I go to "/list_tasks" to add a task')
def step_impl(context):
    #deberia ir en enviroment.py, pero nos falla
    context.browser = webdriver.PhantomJS()
    context.browser.implicitly_wait(1)
    context.server_url = 'https://todolist-ardilom.c9users.io/list_task'
    
    br = context.browser
    br.get(context.base_url + '/list_tasks')

@when(u'I fill in the form "task" with "Buy bread and milk and beer, it\'s friday!!!" and I click in the submit button in the form')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('name').send_keys('Buy bread and milk and beer, it\'s friday!!!')
    br.find_element_by_id('add_submit').click()
    
@then(u'I should see "Buy bread and milk and beer, it\'s friday!!!')
def step_impl(context):
    br = context.browser
    assert "Buy bread and milk and beer, it\'s friday!!!" in br.find_element_by_id('task-1').text
    #deberia ir en enviroment.py, pero nos falla
    context.browser.quit()


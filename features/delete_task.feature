Feature: In order to remember my tasks, as a working person, I want to delete a task
Scenario: Delete task   
  Given I go to "/list_tasks" to delete a task
  When I select the delete button of task "Buy bread and milk and beer, it's friday!!!"
  Then I should no longer be able  to see the task "Buy bread and milk and beer, it's friday!!!" on the list
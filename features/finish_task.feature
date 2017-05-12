Feature: In order to remember my tasks, as a working person, I want to finish a task in the tasks_list

Scenario: Finish a task
  Given I go to "/tasks" to finish a task
  When I fill select the complete button of task "Buy bread and milk and beer, it's friday!!!"
  Then I should be able to see the task "Buy bread and milk and beer, it's friday!!!", as completed.
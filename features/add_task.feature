Feature: In order to remember my tasks, as a working person, I want to add tasks to a task list

Scenario: Create a task
  Given I go to "/tasks" to add a task
  When I fill in the form "task" with "Buy bread and milk and beer, it's friday!!!" and I click in the submit button in the form
  Then I should see "Buy bread and milk and beer, it's friday!!!
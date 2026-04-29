Feature: Dashboard functionality
  As a user, I want to interact with the OrangeHRM dashboard after login

  @regression @dashboard @dashboard1
  @dataFile:data/${env}/loginData.json
  Scenario: Dashboard 01: Dashboard is displayed after successful login
    Given I am on the login page
    When user login with "username" and "password"
    Then I should see the dashboard

  @regression @dashboard @dashboard2
  @dataFile:data/${env}/loginData.json
  Scenario: Dashboard 02: Welcome message is visible on dashboard
    Given I am on the login page
    When user login with "username" and "password"
    Then I should see the welcome message on dashboard

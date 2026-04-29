Feature: Login functionality
  As a user, I want to login to OrangeHRM so that I can access my dashboard

  @regression @scenario1
  Scenario: LoginPage 01: Successful login with valid credentials
    Given I am on the login page
    When I enter valid username and password
    And I click the login button
    Then I should see the dashboard

  @regression @scenario2
  Scenario: LoginPage 02: Successful login using static Data from feature file
    Given I am on the login page
    When user login with static username as "Admin" and password as "admin123"
    Then I should see the dashboard
    
  @regression @scenario3
  @dataFile:data/${env}/loginData.json
  Scenario: LoginPage 03: Successful login using Json Plain Data
    Given I am on the login page
    When user login with "username" and "password"
    Then I should see the dashboard

  @regression @scenario4
  @dataFile:data/${env}/registrationData.json
  Scenario: LoginPage 04: Successful login using nested Json Data
    Given I am on the login page
    When user login with "username" and "password"
    When user enters address information from "address" data
    
  @regression @scenario5 @login
  @dataFile:data/${env}/invalidLoginData.json
  Scenario: Login Page 05: Unsuccessful login with invalid credentials
    Given I am on the login page
    When user login with "username" and "password"
    Then I should see Invalid credentials message
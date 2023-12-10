# Created by user at 12/3/23
Feature: Sign In Tests


  Scenario: User Signin
    Given Open Home Page
    When Hover over Signin Link
    And Click Signin Button
    When Input chriscrayton20@gmail.com in email field
    And Input testing#24 in password field
    When Click popup signin button
    And Hover over signin icon
    Then Verify user is signed in

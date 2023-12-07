# Created by user at 10/15/23
Feature: New Header Tests
  # Enter feature description here


    Scenario: Verify All New Link is present
    Given Open Home Page
    When Hover over New header link
    And Click All New Link
    Then Verify New page is opened8

    Scenario: Verify Just Dropped Link is present
    Given Open Home Page
    When Hover over New header link
    And Click Just Dropped Link
    Then Verify Just Dropped page is opened

    Scenario: Verify Next Big Thing Link is present
    Given Open Home Page
    When Hover over New header link
    And Click The Next Big Think Link
    Then Verify The Next Big Thing page is opened9

    Scenario: Verify Bestsellers page is present
    Given Open Home Page
    When Hover over New header link
    And Click Bestseller Link
    Then Verify Bestsellers page is opened10

    Scenario: Verify Trending on Social page is present
    Given Open Home Page
    When Hover over New header link
    And Click Trending on Social Link
    Then Verify Trending at Sephora page is present11

#    Scenario: Verify Trending on Social page is present
#    Given Open Home Page
#    When Hover over New header link
#    And Click Trending on Social Link
#    Then Verify Trending at Sephora page is present11

#    Scenario: Verify Holiday Gift Guide Link is present
#    Given Open Home Page
#    When Hover over New header link
#    And Click Holiday Gift Guide Link
#    Then Verify Gift Guide page is opened7
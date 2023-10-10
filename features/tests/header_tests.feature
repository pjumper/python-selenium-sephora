# Created by user at 9/29/23
Feature: Header Tests Functionality


  Scenario: Verify header links are present
    Given Open Home Page
    Then Verify main header has 12 links

  Scenario: Verify new header links are present
    Given Open Home Page
    When Hover over New header link
    When Click ALL NEW link
    Then Verify New page has 7 links

    Scenario: Verify Just Dropped Link is present
    Given Open Home Page
    When Hover over New header link
    And Click Just Dropped Link
    Then Verify Just Dropped page is opened

  Scenario: Verify Makeup Link is present
    Given Open Home Page
    When Hover over New header link
    And Click Makeup link
    Then Verify New Makeup page is opened1

  Scenario: Verify Makeup Link is present
    Given Open Home Page
    When Hover over New header link
    And Click New Skincare link
    Then Verify New Skincare page is opened2
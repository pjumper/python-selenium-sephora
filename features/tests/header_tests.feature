# Created by user at 9/29/23
Feature: Header Tests Functionality


  Scenario: Verify header links are present
    Given Open Home Page
    Then Verify main header has 12 links

  Scenario: Verify new header links are present
    Given Open Home Page
    When Click New header link
    Then Verify New page has 7 links

#    Scenario: Verify Just Dropped Link is present
#    Given Open Home Page
#    When Click New header link
#    #And Click Just Dropped Link

# Created by user at 9/29/23
Feature: New Header Tests Functionality


  Scenario: Verify header links are present
    Given Open Home Page
    Then Verify main header has 12 links

#  Scenario: Verify new header links are present
#    Given Open Home Page
#    When Hover over New header link
#    When Click ALL NEW link
#    Then Verify New page has 7 links

  Scenario: Verify new header links are present
    Given Open Home Page
    When Hover over New header link
    Then Verify new header has 17 links



  Scenario: Verify New Makeup Link is present
    Given Open Home Page
    When Hover over New header link
    And Click Makeup link
    Then Verify New Makeup page is opened1

  Scenario: Verify New Skincare Link is present
    Given Open Home Page
    When Hover over New header link
    And Click New Skincare link
    Then Verify New Skincare page is opened2

  Scenario: Verify New Haircare Link is present
    Given Open Home Page
    When Hover over New header link
    And Click New Haircare link
    Then Verify New Hair page is opened3

  Scenario: Verify New Fragrance Link is present
    Given Open Home Page
    When Hover over New header link
    And Click New Fragrance link
    Then Verify New Fragrance page is opened4

  Scenario: Verify Bath & Body Link is present
    Given Open Home Page
    When Hover over New header link
    And Click New Bath & Body link
    Then Verify New Bath & Body page is opened5

  Scenario: Verify New Tools & Brushes Link is present
    Given Open Home Page
    When Hover over New header link
    And Click New Tools & Brushes link
    Then Verify New Tools & Brushes page is opened6
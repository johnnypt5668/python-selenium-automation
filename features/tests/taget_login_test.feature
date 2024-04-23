# Created by johnharchar at 4/2/24
Feature: Target login test
  # Enter feature description here

  Scenario: Verify login is functional
    Given Open Target main page
    When Click on header login
    Then Click on side login
    Then Verify sign in page is open
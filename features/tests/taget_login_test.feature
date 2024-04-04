# Created by johnharchar at 4/2/24
Feature: Target login test
  # Enter feature description here

  Scenario: Verify login is functional
    Given Target homepage is open
    When Click on login on top and on side
    Then Verify sign in page is open
# Created by johnharchar at 4/2/24
Feature: Target site checks
  # Enter feature description here

  Scenario: Verify cart is empty
    Given Target home page is open
    When Click on cart logo in top corner
    Then Verify cart is empty
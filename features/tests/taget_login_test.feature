# Created by johnharchar at 4/2/24
Feature: Target login test
  # Enter feature description here

  Scenario: Verify login is functional
    Given Open Target main page
    When Click on header login
    Then Click on side login
    Then Verify sign in page is open

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Click on header login
    Then Click on side login
    And Store original login window
    And Click on Target terms and conditions link
    And Switch to newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original

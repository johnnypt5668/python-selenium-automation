# Created by johnharchar at 4/2/24
Feature: Target site checks
  # Enter feature description here

  Scenario: Verify cart is empty
    Given Open Target main page
    When Click on Cart icon
    Then Verify cart empty message

  Scenario: User can put item into cart
    Given Open Target main page
    When Search for 'coffee'
    Then Place item in cart
    And Verify item is in cart
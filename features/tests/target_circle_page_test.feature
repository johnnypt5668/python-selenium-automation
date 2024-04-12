# Created by johnharchar at 4/9/24
Feature: Target Circle page test
  # Enter feature description here

  Scenario: Verify Benefits elements are on page
    Given Open Target main page
    When Click on Target page link
    Then Verify 5 links in benefits section
    # Enter steps here
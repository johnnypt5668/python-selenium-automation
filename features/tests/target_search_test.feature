# Created by johnharchar at 4/9/24
Feature: Search tests
  # Enter feature description here

  Scenario Outline: User can search for products
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    Examples:
    |item         |expected_item  |
    |coffee       |coffee         |
    |tea          |tea            |
    |mug          |mug            |
    # Enter steps here


  #  Given Open Target main page
  #  When Search for 'tea'
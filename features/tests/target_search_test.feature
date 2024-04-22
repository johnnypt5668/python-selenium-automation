# Created by johnharchar at 4/9/24
Feature: Search tests
  # Enter feature description here

  Scenario: User can search for a coffee
    Given Open Target main page
    When Search for coffee
    Then Verify search results are shown for coffee

  Scenario: User can search for a tea
    Given Open Target main page
    When Search for tea
    Then Verify search results are shown for tea



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

Scenario: Verify user can see product names and images
  Given Open Target main page
  When Search for 'AirPods (3rd Generation)'
  Then Verify every product has a name and image
  #  Given Open Target main page
  #  When Search for 'tea'
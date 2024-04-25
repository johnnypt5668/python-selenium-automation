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
    Then Verify that URL has tea


  Scenario Outline: User can search for products
    Given Open Target main page
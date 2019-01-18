Feature: Photo Gallery Management REST API

  Scenario: Get all Photo Galleries
    Given we have at least one gallery record
     When we retrieve the available galleries
     Then the API will return all of them

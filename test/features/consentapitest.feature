@consentapitest @duckduckgo
Feature: MCC Consent BB API Integration Testing  
  As a API Integration Team,
  I want to Test Coonsent BB API Specs and Endpoint of Consent BB App Services.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Test Consent BB API POST Request Service  
    Given the URL of Consent BB API is queried   
    #When the user searches for "root"
    When the required data is posted to get consent request and token  
    Then the response status code on succesfull post operation is "200"
    #Then the check for the auth token recieved for further processing  
    

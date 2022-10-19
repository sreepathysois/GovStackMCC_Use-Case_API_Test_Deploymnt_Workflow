@registerusertest @duckduckgo
Feature: MCC Register User API Integration Testing  
  As a API Integration Team,
  I want to Test Register Mother and Child Specs and Endpoint of MCC BB App Services.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Test Registration API POST Request Service  
    Given the URL of Register User API is queried   
    #When the user searches for "root"
    When the required details is posted to register user for MCC Project 
    Then the response status code on succesfull post operation is "200"
    #Then the check for the auth token recieved for further processing  
    

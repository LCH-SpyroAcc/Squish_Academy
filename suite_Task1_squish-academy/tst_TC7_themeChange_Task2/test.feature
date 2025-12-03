Feature: Coffee machine functional testing

	Background:
	    Given test application is running
        When Start screen elements are displayed
        Then I click to start

    Scenario: CoffeeMachine UI test
		 Then Verify theme button on dark
		 Then Verify theme button on bright
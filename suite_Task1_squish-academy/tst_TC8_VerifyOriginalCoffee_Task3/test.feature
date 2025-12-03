Feature: Coffee machine functional testing

	Background:
	    Given test application is running
        When Start screen elements are displayed
        Then I click to start

    Scenario: Verify every original settings of coffee
		 And 'Cappuccino' card displays 'Milk, Espresso, Foam' ingredients and 2 Mins preparation time
		 Then selected coffee settings are original
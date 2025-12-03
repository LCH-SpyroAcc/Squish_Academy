Feature: Coffee machine functional testing

	Background:
	    Given test application is running
        When Start screen elements are displayed
        Then I click to start

    Scenario: Capuccino make user scenario
         When I click on cappucino button
		 Then cappucino make screen is displayed
		 And user can decrease foam and add sugar to his cappucino

Feature: Coffee machine functional testing

    Background:
        Given test application is running
        When Start screen elements are displayed
        Then I click to start

    Scenario: Making espresso user scenario
         When I click on espresso button
		 Then espresso make screen is displayed
		 And user can increase amount of coffee and add foam to his espresso
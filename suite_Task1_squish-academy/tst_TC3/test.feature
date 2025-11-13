Feature: Coffee machine functional testing

    Scenario: Making espresso user scenario
        Given test application is running
         When I click on espresso button
		 Then espresso make screen is displayed
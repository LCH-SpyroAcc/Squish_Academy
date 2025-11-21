Feature: Coffee machine functional testing

    Scenario: Making espresso user scenario
        Given test application is running
         When I click on espresso button
		 Then espresso make screen is displayed
		 And user can increase amount of coffee and add foam to his espresso
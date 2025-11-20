Feature: Coffee machine functional testing with screenshot comparison

    Scenario: Capuccino make user scenario
        Given test application is running
         When I click on cappucino button
		 Then cappucino make screen is displayed
		 And I verify if application match reference screenshot
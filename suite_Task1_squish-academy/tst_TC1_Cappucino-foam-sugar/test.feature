Feature: Coffee machine functional testing

    Scenario: Capuccino make user scenario
        Given test application is running
         When I click on cappucino button
		 Then cappucino make screen is displayed
		 And user can decrease foam and add sugar to his cappucino

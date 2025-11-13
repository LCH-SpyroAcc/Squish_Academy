Feature: Coffee machine functional testing E2E

    Scenario: Making latte user scenario end to end
        Given test application is running
         When I click on latte button
		 Then latte make screen is displayed
		 Then brewing is started
		 Then coffee is ready
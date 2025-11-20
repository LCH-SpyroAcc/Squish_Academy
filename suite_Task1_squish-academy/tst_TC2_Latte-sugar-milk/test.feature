Feature: Coffee machine functional testing

    Background:
        Given test application is running

    Scenario: Latte make user scenario with 2p of sugar and milk addition
         When I click on latte button
		 Then latte make screen is displayed
		 And user can add sugar and milk to his Latte

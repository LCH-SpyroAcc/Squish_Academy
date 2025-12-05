Feature: Coffee machine functional testing

	Background:
	    Given test application is running
        When Start screen elements are displayed
        Then I click to start

    Scenario: Verify every original settings of coffee
		 Then 'Cappuccino' card displays 'Milk, Espresso, Foam' ingredients and 2 Mins preparation time
		 And 'Latte' card displays 'Coffee, Foam' ingredients and 3 Mins preparation time
		 And 'Espresso' card displays 'Milk, Espresso' ingredients and 2 Mins preparation time
		 And 'Macchiato' card displays 'Milk foam, Espresso' ingredients and 4 Mins preparation time
		 Then 'Cappucino' card displays additions '|60/60/60/0|' which is original
		 And 'Latte' card displays additions '|40/20/60/0|' which is original
		 And 'Espresso' card displays additions '|80/0/0/0|' which is original
		 And 'Macchiato' card displays additions '|100/5/10/0|' which is original

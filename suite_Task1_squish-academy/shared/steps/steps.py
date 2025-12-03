# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import names

@Given("test application is running")
def step(context):
    startApplication("coffeemachine")
    test.log("Coffee machine is running")
    #mouseClick(waitForObject(names.homeScreen_getStartedButton_text), MouseButton.LeftButton)

@When("Start screen elements are displayed")
def step(context):

    welcome_screen_elements = [
        names.homeScreen_coffeMachine_text,
        names.homeScreen_coffeeCup_image,
        names.homeScreen_flavorText_text,
        names.homeScreen_getStartedButton_text,
        names.homeScreen_getStartedButton_icon
    ]
    
    for element in welcome_screen_elements:
        if waitForObject(element):
            test.passes(f"Element found: {element}")
            #mouseClick(waitForObject(names.homeScreen_getStartedButton_text), MouseButton.LeftButton)
            
@Then("I click to start")
def step(context):
    mouseClick(waitForObject(names.homeScreen_getStartedButton_text), MouseButton.LeftButton)

@When("I click on cappucino button")
def step(context):
    cappucino_choosen = mouseClick(waitForObject(names.button_AbstractButton), MouseButton.LeftButton)

@When("I click on latte button")
def step(context):
    latte_choosen = mouseClick(waitForObject(names.button_AbstractButton_2), MouseButton.LeftButton)
    
@When("I click on espresso button")
def step(context):
    espresso_choosen = mouseClick(waitForObject(names.button_AbstractButton_3), MouseButton.LeftButton)
    
@When("I click on macchiato button")
def step(context):
    macchiato_choosen = mouseClick(waitForObject(names.button_AbstractButton_4), MouseButton.LeftButton)

@Then("cappucino make screen is displayed")
def step(context):
    test.compare(str(waitForObjectExists(names.coffee_Cappuccino_Text).text), "Cappuccino")
    test.compare(waitForObjectExists(names.coffee_Cappuccino_Text).visible, True)    

@Then("latte make screen is displayed")
def step(context):
    test.compare(str(waitForObjectExists(names.coffee_Latte_Text).text), "Latte")
    test.compare(waitForObjectExists(names.coffee_Latte_Text).visible, True)

@Then("espresso make screen is displayed")
def step(context):
    test.compare(str(waitForObjectExists(names.coffee_Espresso_Text).text), "Espresso")
    test.compare(waitForObjectExists(names.coffee_Espresso_Text).visible, True)
    
@Then("macchiato make screen is displayed")
def step(context):
    test.compare(str(waitForObjectExists(names.coffee_Macchiato_Text).text), "Macchiato")
    test.compare(waitForObjectExists(names.coffee_Macchiato_Text).visible, True) 

@Then("brewing is started")
def step(context):
    mouseClick(waitForObject(names.confirmButton_CustomButton), MouseButton.LeftButton)
    test.compare(str(waitForObjectExists(names.continue_Text).text), "Continue")
    test.compare(waitForObjectExists(names.continue_Text).visible, True)
    mouseClick(waitForObject(names.continue_Text), MouseButton.LeftButton)
    test.compare(str(waitForObjectExists(names.brewing_Text).text), "Brewing...")
    test.compare(waitForObjectExists(names.brewing_Text).visible, True)

@Then("coffee is ready")
def step(context):
    test.compare(waitForObjectExists(names.coffee_QQuickApplicationWindow).visible, True)   
    
@Then("user can add sugar and milk to his Latte")
def step(context):
    mouseClick(waitForObject(names.o_MultiEffect_2), 313, 291, Qt.LeftButton) #set sugar
    mouseClick(waitForObject(names.o_MultiEffect_2), 484, 128, Qt.LeftButton) #set milk
    test.compare(waitForObjectExists(names.sugar_Image).opacity, 0.5) #check sugar
    test.compare(waitForObjectExists(names.milk_Image).opacity, 1) #check milk

@Then("user can increase amount of coffee and add foam to his espresso")
def step(context):
    mouseClick(waitForObject(names.o_MultiEffect_2), 482, 49, Qt.LeftButton) #amount of coffee
    mouseClick(waitForObject(names.o_MultiEffect_2), 204, 209, Qt.LeftButton) #add foam
    test.compare(waitForObjectExists(names.coffee_Image).opacity, 1) #check ml of coffee
    test.compare(waitForObjectExists(names.foam_Image).opacity, 1) #check if foam is added
    
@Then("user can decrease foam and add sugar to his cappucino")
def step(context):
    mouseClick(waitForObject(names.o_MultiEffect_2), 478, 292, Qt.LeftButton) #set foam
    mouseClick(waitForObject(names.o_MultiEffect_2), 315, 209, Qt.LeftButton) #set sugar
    test.compare(waitForObjectExists(names.foam_Image).opacity, 1) #check if foam is decreased
    test.compare(waitForObjectExists(names.sugar_Image).opacity, 1) #check sugar
    
@Then("Verify theme button on dark")
def step(context):
    #mouseClick(waitForObject(names.theme_button), Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.chooseCoffee_text).text), "Coffee Selection")
    test.compare(waitForObjectExists(names.chooseCoffee_text).color, "#fefefe")

@Then("Verify theme button on bright")
def step(context):
    mouseClick(waitForObject(names.theme_button), Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.chooseCoffee_text).text), "Coffee Selection")
    test.compare(waitForObjectExists(names.chooseCoffee_text).color, "#121111")
    
    

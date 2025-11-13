# encoding: UTF-8

from objectmaphelper import *

coffee_QQuickApplicationWindow = {"title": "Coffee", "type": "QQuickApplicationWindow", "unnamed": 1, "visible": True}
coffee_ChoosingCoffee = {"container": coffee_QQuickApplicationWindow, "type": "ChoosingCoffee", "unnamed": 1, "visible": True}
button_AbstractButton = {"checkable": True, "container": coffee_ChoosingCoffee, "id": "button", "type": "AbstractButton", "unnamed": 1, "visible": True}
o_MultiEffect = {"container": coffee_ChoosingCoffee, "occurrence": 2, "type": "MultiEffect", "unnamed": 1, "visible": True}
coffee_home_Home = {"container": coffee_QQuickApplicationWindow, "id": "home", "type": "Home", "unnamed": 1, "visible": True}
home_getStartedButton_CustomButton = {"checkable": False, "container": coffee_home_Home, "id": "getStartedButton", "type": "CustomButton", "unnamed": 1, "visible": True}
home_Get_Started_Text = {"container": coffee_home_Home, "text": "Get Started", "type": "Text", "unnamed": 1, "visible": True}
coffee_Cappuccino_Text = {"container": coffee_QQuickApplicationWindow, "text": "Cappuccino", "type": "Text", "unnamed": 1, "visible": True}
button_AbstractButton_2 = {"checkable": True, "container": coffee_ChoosingCoffee, "id": "button", "occurrence": 2, "type": "AbstractButton", "unnamed": 1, "visible": True}
coffee_Settings = {"container": coffee_QQuickApplicationWindow, "type": "Settings", "unnamed": 1, "visible": True}
cup_Image = {"container": coffee_Settings, "id": "cup", "source": "./images/Cups/dark_cup.svgz", "type": "Image", "unnamed": 1, "visible": True}
coffee_Latte_Text = {"container": coffee_QQuickApplicationWindow, "text": "Latte", "type": "Text", "unnamed": 1, "visible": True}
o_MultiEffect_2 = {"container": coffee_Settings, "type": "MultiEffect", "unnamed": 1, "visible": True} #SUGAR 2P
coffee_Espresso_Text = {"container": coffee_QQuickApplicationWindow, "text": "Espresso", "type": "Text", "unnamed": 1, "visible": True}
coffee_Macchiato_Text = {"container": coffee_QQuickApplicationWindow, "text": "Macchiato", "type": "Text", "unnamed": 1, "visible": True}
button_AbstractButton_3 = {"checkable": True, "container": coffee_ChoosingCoffee, "id": "button", "occurrence": 3, "type": "AbstractButton", "unnamed": 1, "visible": True}
button_AbstractButton_4 = {"checkable": True, "container": coffee_ChoosingCoffee, "id": "button", "occurrence": 4, "type": "AbstractButton", "unnamed": 1, "visible": True}
confirmButton_CustomButton = {"checkable": False, "container": coffee_Settings, "id": "confirmButton", "type": "CustomButton", "unnamed": 1, "visible": True}
coffee_Insert = {"container": coffee_QQuickApplicationWindow, "type": "Insert", "unnamed": 1, "visible": True}
o_MultiEffect_3 = {"container": coffee_Insert, "type": "MultiEffect", "unnamed": 1, "visible": True}
continue_Text = {"container": coffee_Insert, "text": "Continue", "type": "Text", "unnamed": 1, "visible": True}
coffee_Ready = {"container": coffee_QQuickApplicationWindow, "type": "Ready", "unnamed": 1, "visible": True}
o_MultiEffect_4 = {"container": coffee_Ready, "type": "MultiEffect", "unnamed": 1, "visible": True}
coffee_Progress = {"container": coffee_QQuickApplicationWindow, "type": "Progress", "unnamed": 1, "visible": True}
o_MultiEffect_5 = {"container": coffee_Progress, "type": "MultiEffect", "unnamed": 1, "visible": True}
cup_Image_2 = {"container": coffee_Ready, "id": "cup", "source": "./images/Cups/dark_cup.svgz", "type": "Image", "unnamed": 1, "visible": True}
brewing_Text = {"container": coffee_Progress, "text": "Brewing...", "type": "Text", "unnamed": 1, "visible": True}
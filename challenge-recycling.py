#Sefa started a recycling service at his school. To help it succeed, he’s building an app where students can enter information about an item, and then the app tells them whether it belongs in the trash or in the recycling. Sefa wants to start the service by recycling plastic.

#Add a conditional that sets waste_type to the value "recycling" if the item is plastic.
#An item is plastic if the variable material contains the value "plastic". For all other materials, waste_type should contain "trash".

	#add: 2. Large plastic items should go in the recycling, small plastic items should go in the trash, and all other items should go in the trash.

material = input("What material is it? ")

waste_type = "trash"
# if it is plastic
if material == "plastic":
        waste_type = "recycling"
        length = float(input("What is its length in cm? "))
        if length <= 10:
                waste_type = "trash"
        
    
    

print("Please deposit your item in the " + waste_type + " bin.")


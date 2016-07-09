from Address import Address

def main():
        inputType = str(input("Enter 1 for batch processing or 2 for manual input: "))
        if (inputType == "2"):
                enterNewAddress = True
                while(enterNewAddress):
                        address = getInput()
                        print("---------------------")
                        print("Entered address: " + address.formatOutput())
                        if(address.isCompleteAddress()):
                                address.normalize()
                                print("Normalized address: " + address.formatOutput())
                        else:
                                print("Incomplete address entered. Could not normalize.")
                        continueManual = str(input("Enter 1 to enter another address or any other key to close the program."))
                        if(continueManual != "1"):
                                enterNewAddress = False

                
        elif (inputType == "1"):
                addressFileName = str(input("Enter the name and location of the file you wish to process:" ))
                properOutputFileName = str(input("Enter the name and location of the file you wish to hold properly formatted addresses:"))
                errorOutputFileName = str(input("Enter the name and location of the file you wish to hold addresses that can't be normalized:"))
                addressFile = open(addressFileName, 'r')
                properOutputFile = open(properOutputFileName, 'w')
                errorOutputFile = open(errorOutputFileName, 'w')
                for line in addressFile:
                        address = parse(line)
                        if(address.isCompleteAddress()):
                                address.normalize()
                                properOutputFile.write(address.formatOutput() + '\n')
                        else:
                                errorOutputFile.write(address.formatOutput() + '\n')
                addressFile.close()
                properOutputFile.close()
                errorOutputFile.close()
                print("Processing completed.")
 
def getInput():
	street = str(input("Enter the street: "))
	city = str(input("Enter the city: "))
	state = str(input("Enter the state: "))
	zipCode = str(input("Enter the zip: "))
	address = Address(street, city, state, zipCode)
	return address

def parse(line):
        addressParts = line.split('\t')
        return Address(addressParts[0], addressParts[1], addressParts[2], addressParts[3])
	
main()

# Manage_Riverbed_AppResponses

This is a repository to get configuration data from multiple Riverbed AppResponse 11 (AR11) and present them in a spreadsheet. 
There is a main script "Manage_ARs_RO" which requires two other libraries to work, “appresponse_device.py” and “appresponse_mgmt_api.py”, both of which are part of this github repository “https://github.com/nickhurst10/Manage_Riverbed_AppResponses.git”.
“appresponse_mgmt_api.py” interacts with the AR11 to do the restAPI GET requests.
“appresponse_device.py” manages the interaction between the main script and “appresponse_mgmt_api.py” library.

For the script to know what AR11's to access, this script looks for a file called “ar_list.csv” and looks for IP addresses under the header “ar_list”. An example is include in the github repository.

To run the script, the user must provide user credentials, which have the relevant access to all the AR11’s.

This script was tested on python version 3.9, on linux and MACOS.

Example to run the script
	python3 Manage_ARs_RO.py -u username

After which the user will be prompted to enter their password.

If you have any questions, please reach out to me.

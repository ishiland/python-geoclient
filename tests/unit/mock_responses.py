# Slimmed down mock responses from the Geoclient API

address_response = {
    'address': {'bblBoroughCode': '1', 'boePreferredStreetName': 'WORTH STREET', 'houseNumber': '125'}}

address_zip_response = {
    'address': {'boePreferredStreetName': 'WORTH STREET', 'houseNumber': '125', 'zipCodeIn': '10013'}}

bbl_response = {
    'bbl': {'bblBoroughCode': '1', 'bblTaxBlock': '00168', 'bblTaxLot': '0032'}}

bin_response = {
    'bin': {'bblTaxBlock': '00168', 'bblTaxLot': '0032', 'buildingIdentificationNumber': '1001831'}}

blockface_response = {
    'blockface': {'firstStreetNameNormalized': 'LAFAYETTE STREET', 'secondStreetNameNormalized': 'WORTH STREET'}}

intersection_response = {
    'intersection': {'lionNodeNumber': '0015490', 'numberOfIntersectingStreets': '2'}}

place_response = {
    'place': {'boePreferredStreetName': 'EMPIRE STATE BUILDING',
              'message': '350 5 AVENUE IS THE UNDERLYING ADDRESS OF EMPIRE STATE BUILDING'}}

search_response = {
    'results': [{'level': '1', 'status': 'POSSIBLE_MATCH',
                 'request': 'place [name=Empire State Building, borough=MANHATTAN, zip=null]',
                 'response': {'message': '350 5 AVENUE IS THE UNDERLYING ADDRESS OF EMPIRE STATE BUILDING'}}]}

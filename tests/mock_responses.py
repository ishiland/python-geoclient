# Slimmed down mock responses from the Geoclient API

address_response = {
    u'address': {u'bblBoroughCode': u'1', u'boePreferredStreetName': u'WORTH STREET', u'houseNumber': u'125',
                 u'geosupportReturnCode': u'00'}
}

address_zip_response = {
    u'address': {u'boePreferredStreetName': u'WORTH STREET', u'houseNumber': u'125', u'zipCodeIn': u'10013',
                 u'geosupportReturnCode': u'00'
                 }}

bbl_response = {
    u'bbl': {u'bblBoroughCode': u'1', u'bblTaxBlock': u'00168', u'bblTaxLot': u'0032', u'geosupportReturnCode': u'00'}}

bin_response = {
    u'bin': {u'bblTaxBlock': u'00168', u'bblTaxLot': u'0032', u'buildingIdentificationNumber': u'1001831',
             u'geosupportReturnCode': u'00'
             }
}

blockface_response = {
    u'blockface': {u'firstStreetNameNormalized': u'LAFAYETTE STREET', u'secondStreetNameNormalized': u'WORTH STREET',
                   u'geosupportReturnCode': u'00'
                   }

}
intersection_response = {
    u'intersection': {u'lionNodeNumber': u'0015490', u'numberOfIntersectingStreets': u'2',
                      u'geosupportReturnCode': u'00'}}

place_response = {
    u'place': {u'boePreferredStreetName': u'EMPIRE STATE BUILDING',
               u'message': u'350 5 AVENUE IS THE UNDERLYING ADDRESS OF EMPIRE STATE BUILDING',
               u'geosupportReturnCode': u'00'}}

search_response = {
    u'results': [{u'level': u'1', u'status': u'POSSIBLE_MATCH',
                  u'request': u'place [name=Empire State Building, borough=MANHATTAN, zip=null]',
                  u'response': {u'message': u'350 5 AVENUE IS THE UNDERLYING ADDRESS OF EMPIRE STATE BUILDING'},
                  u'geosupportReturnCode': u'00'}]}

# full response
address_response_error = {
    u'address': {u'streetName7': u'WORLD TRADE CENTER EAST CNCRSE', u'streetName5': u'WORLD FINANCIAL CENTER SKYBRIDGE',
                 u'streetCode5': u'10071901', u'streetCode4': u'10093601', u'streetCode7': u'14560116',
                 u'streetCode6': u'14560101', u'streetCode1': u'11191501', u'streetCode3': u'14561201',
                 u'streetCode2': u'14549001', u'reasonCode': u'A',
                 u'message': u"'WORT ST' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.",
                 u'streetName10': u'WORLD TRADE CENTER OCULUS', u'streetCode9': u'11394005',
                 u'streetCode8': u'14560114', u'streetCode10': u'14560118',
                 u'firstStreetNameNormalized': u'WORT STREET', u'streetName1In': u'WORT ST', u'boroughCode1In': u'1',
                 u'message2': u"'WORT ST' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.", u'reasonCode1e': u'A',
                 u'returnCode1a': u'EE', u'reasonCode1a': u'A', u'returnCode1e': u'EE',
                 u'geosupportFunctionCode': u'1B', u'houseNumberSortFormat': u'000125000AA', u'reasonCode2': u'A',
                 u'streetName6': u'WORLD TRADE CENTER', u'crossStreetNamesFlagIn': u'E',
                 u'streetName4': u'WORLD FINANCIAL CENTER FERRY', u'streetName3': u'WORLD FINANCIAL CENTER',
                 u'streetName2': u'WORTH STREET', u'streetName1': u'WORTH SQUARE', u'houseNumberIn': u'125',
                 u'numberOfStreetCodesAndNamesInList': u'10', u'geosupportReturnCode': u'EE',
                 u'streetName9': u'WORLD TRADE CENTER NORTH POOL', u'streetName8': u'WORLD TRADE CENTER NORTH CNCRSE',
                 u'workAreaFormatIndicatorIn': u'C', u'houseNumber': u'125', u'firstBoroughName': u'MANHATTAN',
                 u'geosupportReturnCode2': u'EE'}
}

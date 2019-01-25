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

# 'message' and 'message2' are equal
msg_equal = {
    u'address': {u'message': u"'WORT ST' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.",
                 u'message2': u"'WORT ST' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.",
                 u'geosupportReturnCode': u'EE'}
}

# 'message' and 'message2' are unequal
msg_unequal = {
    u'address': {u'message': u"THIS IS THE FIRST MESSAGE.",
                 u'message2': u"THIS IS THE SECOND MESSAGE",
                 u'geosupportReturnCode': u'EE'}
}

# only 'message' returned
msg_single = {
    u'address': {u'message': u"'WORT ST' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.",
                 u'geosupportReturnCode': u'EE'}
}

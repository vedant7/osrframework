# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#    This program is part of OSRFramework. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

import json
import sys

from osrframework.maltfy.lib.maltego import *
import osrframework.searchengines.google as google

def textToGoogleSearchUri(argv):
    ''' 
        List of URI entities corresponding to the results of a Google Search.

        :param argv:    the text to be searched.

        :return:    Nothing is returned but the code of the entities is created.
    '''
    me = MaltegoTransform()
    #me.parseArguments(argv);
    text = sys.argv[1]

    uriList = google.processSearch(text)
    # This returns a dictionary like the following:
    """
        [{
        'attributes': [],
        'type': 'i3visio.uri',
        'value': 'http://foo.com'
        }, {
        'attributes': [],
        'type': 'i3visio.uri',
        'value': 'http://bar.com'
        }, 
        ...
        ]
    """

    #print json.dumps(entities, indent=2)
    for uri in uriList:
        newEnt = me.addEntity(uri["type"],uri["value"])
        newEnt.setDisplayInformation("<h3>" + uri["value"] +"</h3><p>"+str(uri["attributes"])+"</p>")        
        for extraAtt in uri["attributes"]:
            newEnt.addAdditionalFields(str(extraAtt['type']), str(extraAtt['type']), True, str(extraAtt['value']))    

    # Returning the output text...
    me.returnOutput()

if __name__ == "__main__":
    textToGoogleSearchUri(sys.argv)



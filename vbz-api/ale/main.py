import os
from datetime import datetime
from xml.etree import ElementTree
import requests

# https://opentransportdata.swiss/en/cookbook/departurearrival-display/ 

REQUEST_XML_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8"?>
<Trias version="1.1" xmlns="http://www.vdv.de/trias" xmlns:siri="http://www.siri.org.uk/siri" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <ServiceRequest>
        <siri:RequestTimestamp>2024-02-06T19:35:07.142Z</siri:RequestTimestamp>
        <siri:RequestorRef>API-Explorer</siri:RequestorRef>
        <RequestPayload>
            <StopEventRequest>
                <Location>
                    <LocationRef>
                        <StopPointRef>{bpuic}</StopPointRef>
                    </LocationRef>
                    <DepArrTime>{time}</DepArrTime>
                </Location>
                <Params>
                    <NumberOfResults>1</NumberOfResults>
                    <StopEventType>departure</StopEventType>
                    <IncludePreviousCalls>false</IncludePreviousCalls>
                    <IncludeOnwardCalls>false</IncludeOnwardCalls>
                    <IncludeRealtimeData>true</IncludeRealtimeData>
                </Params>
            </StopEventRequest>
        </RequestPayload>
    </ServiceRequest>
</Trias>
"""

def main():
    if 'OPENTRANSPORTDATA_TOKEN' not in os.environ:
        print('Error: The OPENTRANSPORTDATA_TOKEN is not defined in the environement.')
        return

    # export OPENTRANSPORTDATA_TOKEN="the-key-from-opentransportdata-ch"
    token = os.environ['OPENTRANSPORTDATA_TOKEN']

    time = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ') # "2024-02-06T20:35:07"

    BPUIC = 8591306 # Quellenstrasse

    request_xml = REQUEST_XML_TEMPLATE.replace('{bpuic}', str(BPUIC)).replace('{time}', time);
    # print(request_xml)

    headers = {
    'Content-Type': 'application/xml',
    'Authorization': token,
    }
    r = requests.post('https://api.opentransportdata.swiss/trias2020', headers=headers, data=request_xml)
    # print(r.content)

    root = ElementTree.fromstring(r.content)
    # print(tree)

    # for child in root:
    #     print(child.tag, child.attrib)

    ns = {
        'siri': 'http://www.siri.org.uk/siri',
        'trias': 'http://www.vdv.de/trias'
    }

    # .// is for xpath search in the full tree
    stop_event = root.find('.//trias:StopEvent', ns)
    # print(stop_event)

    departure_time = stop_event.find('.//trias:TimetabledTime', ns)
    print(departure_time.text)
    line_number = stop_event.find('.//trias:PublishedLineName', ns).find('trias:Text', ns)
    print(line_number.text)
    destination = stop_event.find('.//trias:DestinationText', ns).find('trias:Text', ns)
    print(destination.text)

if __name__ == '__main__':
    main()

# xml response, autoamtically formatted
# <?xml version="1.0" encoding="UTF-8"?>\n
# <trias:Trias
#     xmlns:siri="http://www.siri.org.uk/siri"
#     xmlns:trias="http://www.vdv.de/trias"
#     xmlns:acsb="http://www.ifopt.org.uk/ac  sb"
#     xmlns:ifopt="http://www.ifopt.org.uk/ifopt"
#     xmlns:datex2="http://datex2.eu/schema/1_0/1_0" version="1.1">
#     <trias:ServiceDelivery>
#         <siri:ResponseTimestamp>2024-02-06T20:52  :50Z</siri:ResponseTimestamp>
#         <siri:ProducerRef>EFAController10.6.15.15-OJP-EFA01-P</siri:ProducerRef>
#         <siri:Status>true</siri:Status>
#         <trias:Language>de</trias:Language>
#         <tria  s:CalcTime>69
#         </trias:CalcTime>
#         <trias:DeliveryPayload>
#             <trias:StopEventResponse>
#                 <trias:StopEventResponseContext>
#                     <trias:Situations></trias:Situations>
#                 </trias:StopEventResponse  Context>
#                 <trias:StopEventResult>
#                     <trias:ResultId>ID-3D0C6A58-7927-4C9E-AA30-ED8A1535FC2F</trias:ResultId>
#                     <trias:StopEvent>
#                         <trias:ThisCall>
#                             <trias:CallAtStop>
#                                 <trias:StopPointRe  f>8591306
#                                 </trias:StopPointRef>
#                                 <trias:StopPointName>
#                                     <trias:Text>Z\xc3\xbcrich, Quellenstrasse</trias:Text>
#                                     <trias:Language>de</trias:Language>
#                                 </trias:StopPointName>
#                                 <trias:ServiceDeparture>
#                                     <trias:TimetabledTime>2024-02-06T19:35:00Z</trias:TimetabledTime>
#                                 </trias:ServiceDeparture>
#                                 <trias:StopSeqNumber>6</trias:StopSeqNumber>
#                             </trias:CallAtStop>
#                         </tri  as:ThisCall>
#                         <trias:Service>
#                             <trias:OperatingDayRef>2024-02-06</trias:OperatingDayRef>
#                             <trias:JourneyRef>ojp-91-17-E-j24-1-617-TA</trias:JourneyRef>
#                             <trias:LineRef>ojp:91017:E:  R</trias:LineRef>
#                             <trias:DirectionRef>return</trias:DirectionRef>
#                             <trias:Mode>
#                                 <trias:PtMode>tram</trias:PtMode>
#                                 <trias:TramSubmode>cityTram</trias:TramSubmode>
#                                 <trias:Name>
#                                     <tri  as:Text>Tram
#                                     </trias:Text>
#                                     <trias:Language>de</trias:Language>
#                                 </trias:Name>
#                             </trias:Mode>
#                             <trias:PublishedLineName>
#                                 <trias:Text>17</trias:Text>
#                                 <trias:Language>de</trias:Language  >
#                             </trias:PublishedLineName>
#                             <trias:OperatorRef>ojp:3849</trias:OperatorRef>
#                             <trias:Attribute>
#                                 <trias:Text>
#                                     <trias:Text>Niederflureinstieg</trias:Text>
#                                     <trias:Language>de
#                                     </trias:  Language>
#                                 </trias:Text>
#                                 <trias:Code>A__NF</trias:Code>
#                             </trias:Attribute>
#                             <trias:OriginStopPointRef>8591067</trias:OriginStopPointRef>
#                             <trias:OriginText>
#                                 <trias:Text>Z\xc3\xbcric  h, Bahnhofstrasse/HB</trias:Text>
#                                 <trias:Language>de</trias:Language>
#                             </trias:OriginText>
#                             <trias:DestinationStopPointRef>8591428</trias:DestinationStopPointRef>
#                             <trias:DestinationText>
#                                 <trias:Text>Z\xc3\xbcrich, Werdh\xc3\xb6lzli</trias:Text>
#                                 <trias:Language>de</trias:Language>
#                             </trias:DestinationText>
#                         </trias:Service>
#                     </trias:StopEvent>
#                 </trias:StopEv  entResult>
#             </trias:StopEventResponse>
#         </trias:DeliveryPayload>
#     </trias:ServiceDelivery>
# </trias:Trias>

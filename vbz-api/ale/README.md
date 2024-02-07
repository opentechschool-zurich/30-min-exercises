# Get the next tram starting from a specific VBZ stop

- We are using <https://opentransportdata.swiss>.
- You are supposed to send XML and you get XML.
- You need to register and get a token to make requests.
- Find the API for querying the departure time (<https://opentransportdata.swiss/en/cookbook/departurearrival-display/>)
- Copy the XML for the request.
- Use the string as a template, with `{placeholder}` for the dynamic values you want to replace.
- Add the token to an environment variable:  
  export OPENTRANSPORTDATA_TOKEN="the-key-from-opentransportdata-ch"  
  and read it from the Python script
- At first set the time to a fixed value (later you can use `datetime` to get the curren time)
- Use the web to find the BPUIC code of the VBZ stop
- Fill the template with the actual values for `bpuic` and `time`.
- Add the token to the headers that will be sent to the server.
- use _requests_ to send a POST request with the XML string as the `data` (you need to get it through _pip_).
- _Print_ the result as text and use a (online) tool to reformat the XML and make it readable.
- Use _etree_ to parse the string into an XML tree.
- Use _etree_'s `find` to search for the relevant XML elements:
  - with `ns` for the namespaces,
  - with `.//` to get into XPATH _mode_ and search the full tree (not just the immediate children).

As an alternative you can use <https://transport.opendata.ch>:

- You don't need to register (no token needed)
- It uses JSON instead of XML

# La oss nå lage en KML fil!
header = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
"""
punkt_mønster = """  <Placemark>
    <Point>
      <coordinates>{},{},0</coordinates>
    </Point>
  </Placemark>
"""
footer = """</Document>
</kml>"""

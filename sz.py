import imgkit
import urllib.request
import json


class Sz:
    def __init__(self):
        self.gis_json_data = urllib.request.urlopen('https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/2/query?where=Country_Region+%3D+%27Poland%27&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=Confirmed%2CRecovered%2CDeaths&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pgeojson&token=')
        self.html = ''
        self.recovered = 0
        self.deaths = 0
        self.confirmed = 0
        self.recovered_percentage = 0
        self.deaths_percentage = 0
        self.make_png()

    def make_png(self):
        self.set_gis_data(json.load(self.gis_json_data))
        self.set_html()
        imgkit.from_string(self.html, '../orleta/public/sz/img/image.png', {"xvfb": ""})

    def set_html(self):
        html = """
            <html>
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
          integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    <link rel="stylesheet" href="http://sluzbazdrowia.info/css/style.css">
                </head>
                <body>
                <div class="dataForCanvas pt-5">
                    <div class="row mt-5">
                        <div class="col-4 pl-5">
                            <h2>ZAINFEKOWANYCH</h2>
                            <p class="infected" style="font-size: 110px">"""+str(self.confirmed)+"""</p>
                        </div>
                        <div class="col-4">
                            <h2>WYLECZONYCH</h2>
                            <p class="cured" style="font-size: 110px">"""+str(self.recovered)+"""</p>
                            <p class="curedPercentage" style="font-size: 60px">"""+str(self.recovered_percentage)+""" %</p>
                        </div>
                        <div class="col-4">
                            <h2>ZGONÓW</h2>
                            <p class="deaths" style="font-size: 110px">"""+str(self.deaths)+"""</p>
                            <p class="deathsPercentage" style="font-size: 60px">"""+str(self.deaths_percentage)+""" %</p>
                        </div>
                    </div>
                </div>
                </body>
            </html>
        """

        self.html = html

    def set_gis_data(self, gis_data):
        self.confirmed = gis_data['features'][0]['properties']['Confirmed']
        self.recovered = gis_data['features'][0]['properties']['Recovered']
        self.deaths = gis_data['features'][0]['properties']['Deaths']
        self.recovered_percentage = round(self.recovered*100/self.confirmed, 2)
        self.deaths_percentage = round(self.deaths*100/self.confirmed, 2)


sz = Sz()



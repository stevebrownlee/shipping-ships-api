from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line
from views import ShippingShipsView
# from views import list_docks, retrieve_dock
# from views import list_haulers, retrieve_hauler
# from views import list_ships, retrieve_ship



class JSONServer(HandleRequests):

    def determine_view(self, url):
        routes = {
            "docks": ShippingShipsView,
            "haulers": ShippingShipsView,
            "ships": ShippingShipsView,
        }
        matching_class = routes[url["requested_resource"]]
        return matching_class()


    def do_GET(self):
        url = self.parse_url(self.path)

        view_class = self.determine_view(url)
        view_class.get(self, url)

        # if url["requested_resource"] == "docks":
        #     view = ShippingShipsView()
        #     return view.get(self, url)

        # elif url["requested_resource"] == "haulers":
        #     view = ShippingShipsView()
        #     return view.get(self, url)

        # elif url["requested_resource"] == "ships":
        #     view = ShippingShipsView()
        #     return view.get(self, url)

        # else:
        #     return self.response("", status.CLIENT_ERROR_RESOURCE_NOT_FOUND_404.value)










#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()
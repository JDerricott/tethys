from tethys_sdk.base import TethysAppBase, url_map_maker


class Arcgistest(TethysAppBase):
    """
    Tethys app class for arcgistest.
    """

    name = 'arcgistest'
    index = 'arcgistest:home'
    icon = 'arcgistest/images/icon.gif'
    package = 'arcgistest'
    root_url = 'arcgistest'
    color = '#8e44ad'
    description = 'this is my second attempt'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='arcgistest',
                controller='arcgistest.controllers.home'
            ),
            UrlMap(
                name='service2',
                url='service2',
                controller='arcgistest.controllers.service2'
            ),
        )

        return url_maps

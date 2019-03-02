from tethys_sdk.base import TethysAppBase, url_map_maker


class Appname(TethysAppBase):
    """
    Tethys app class for Go Connected.
    """

    name = 'Go Connected'
    index = 'appname:home'
    icon = 'appname/images/icon.gif'
    package = 'appname'
    root_url = 'appname'
    color = '#ff8ceb'
    description = 'This app lets you determinenvenient your commute will be.'
    tags = 'Transportation'
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
                url='appname',
                controller='appname.controllers.home'
            ),
        )

        return url_maps

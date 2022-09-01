import os
website_test = "https://cloud.google.com/solutions/web-hosting"
favicon_url_test = "https://www.gstatic.com/devrel-devsite/prod/v5e8a33c76fc7f2ff582bc05b8beea48bc2f986ca4005c00b50180391fed04c56/cloud/images/favicons/onecloud/favicon.ico"

dir_path = os.path.dirname(os.path.realpath(__file__))
assets_path = os.path.join(dir_path, "assets")
favicon_file_location_test = os.path.join(assets_path, "favicon_test.ico")



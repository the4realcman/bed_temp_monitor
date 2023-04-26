from setuptools import setup

plugin_identifier = "bed_temp_monitor"
plugin_package = "octoprint_{}".format(plugin_identifier)
plugin_name = "OctoPrint-{}".format(plugin_identifier)
plugin_version = "1.0.0"
plugin_description = "Monitors bed temperature and waits for it to reach a specific value before resuming operation."
plugin_author = "Cameron Koll"
plugin_author_email = "your.email@example.com"
plugin_url = "https://github.com/yourusername/octoprint_bed_temp_monitor"
plugin_license = "AGPLv3"

setup(
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    author_email=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    packages=[plugin_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "OctoPrint"
    ],
    entry_points={
        "octoprint.plugin": [
            "{} = {}:{}".format(plugin_identifier, plugin_package, plugin_package)
        ]
    }
)

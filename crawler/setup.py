#!/usr/bin/env python
#
#    Copyright (c) 2012 Diego Hernandez Ruiz. All rights reserved.
#    This program is free software: you can redistribute it and/or modify
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

from setuptools import setup, find_packages
setup (name="Diego_MSWL_WebCrawler",
	version=" 0.1",
	packages = find_packages () ,
	scripts = [ 'diego_MSWL_crawler'] ,
	install_requires = ['BeatifulSoup'] ,
	package_data = {'diego_crawler/': [ ''] , } ,
	author = " Diego Hernandez Ruiz " ,
	author_email = " diego.herna@gmail.com" ,
	description = " Scrapper for The New Atlantis " ,
	license = "GNU GPLv3 " ,
	keywords = "web crawler " ,
	url = "https://github.com/donaldyo " ,
	long_description = "This is a project of the subject Development Tools of Master In Juan Carlos I " ,
	download_url = "https://github.com/donaldyo/Development-Tools/tarball/master" , )


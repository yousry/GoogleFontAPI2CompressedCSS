#!/usr/bin/python

# CSSFontCompressor
# Developed with python 3.5.2
# http://www.pyregex.com/ used for regex creatin

# API URL Example
# <link href="https://fonts.googleapis.com/css?family=Baloo+Bhaina|Yatra+One" rel="stylesheet"> 
# Call CSSFontCompressor.py -o fonts.css.gz "https://fonts.googleapis.com/css?family=Baloo+Bhaina|Yatra+One"

# (c) 2016 Yousry Abdallah

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys, getopt, urllib.request, re, base64, gzip

def usage():
	print("Usage: CSSFontCompressor.py [OPTION] URL")
	print("Create css with embedded fonts from Googles font api." )
	print()
	print("\t-o, --outfile\tCSS Name")

def main(argv):
	result = ''
	try:
		opts, args = getopt.getopt(argv, 'ho:',["help", "outfile="])
	except:
		print(str(err))
		usage()
		sys.exit(2)
	outfile = "fonts.css.gz"
	for o, a in opts:
		if o in ("-o", "--outfile"):
			outfile = a
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		else:
			assert False
	if len(args) != 1:
		print("Wrong number of arguments.")
		sys.exit(2)
	url = args[0]
	print("URL: " + url)
	origCSS = ''
	try:
		response = urllib.request.urlopen(url)
		data = response.read()  
		origCSS = data.decode('utf-8') 
	except:
		print(str(err))
		sys.ext(2)
	lines = origCSS.splitlines()
	pUrl = re.compile('^src:.*url\((.*)\) format\(\'(.*)\'\).*$')

	for line in lines:
		stripLine = line.strip()
		if stripLine.startswith("src:"):
			m = pUrl.match(stripLine)
			if m is None:
				print("Could not identify font URL")
				sys.exit(2)
			fontURL = m.group(1)
			fontType = m.group(2)
			data = ''
			try:
				response = urllib.request.urlopen(fontURL)
				data = response.read()  
			except:
				print(str(err))
				sys.ext(2)
			result += 'src: url(data:font/'
			result += fontType
			result += ';base64,'
			result += base64.b64encode(data).decode("utf-8")
			result += ');\n'
		else:
			result += stripLine
			result += '\n'

	resultCompressed = gzip.compress(bytes(result, 'utf-8'))
	with open(outfile, 'wb') as f:
	    f.write(resultCompressed)


if __name__ == '__main__':
	main(sys.argv[1:])
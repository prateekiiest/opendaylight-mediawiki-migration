import requests
import urllib
from xml.etree import ElementTree as ET
import subprocess
import os

S = requests.Session()


#project_name  = ["USC", "Link_Aggregation_Control_Protocol", "CAPWAP", "Time_Series_Data_Repository"]
page_name  = raw_input()

URL = "https://wiki.opendaylight.org/api.php?action=query&prop=revisions&titles=API|" + page_name + "&rvprop=timestamp|user|comment|content&format=xml"

# For examples for migration of any project proposals
# URL = "https://wiki.opendaylight.org/api.php?action=query&prop=revisions&titles=API|Project_Proposals:"+ project_name[0] +"&rvprop=timestamp|user|comment|content&format=xml"


R = S.get(url=URL)
DATA = urllib.urlopen (URL).read()
d = (DATA).strip()

rev = ET.fromstring(d).find('query/pages/page/revisions/rev')
if rev is not None:
  foldername = raw_input()
  filename = foldername + "/" + name.lower() + ".wiki"
  f = open(filename, "w")
  f.write((rev.text).encode("utf-8"))
  f.close()


fileout = foldername + "/" + name.lower() + ".rst"
args = ['pandoc',  '--from', 'mediawiki', '--to', 'rst', filename, '-o', fileout]

subprocess.check_call(args)
os.remove(filename)

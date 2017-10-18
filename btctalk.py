from lxml import html
import requests
import sys

print """
  bitcointalk.org intelligence scraping data
   _     _       _        _ _    _       _   
  | |__ | |_ ___| |_ __ _| | | _(_)_ __ | |_ 
  | '_ \| __/ __| __/ _` | | |/ | | '_ \| __|
  | |_) | || (__| || (_| | |   <| | | | | |_ 
  |_.__/ \__\___|\__\__,_|_|_|\_|_|_| |_|\__|

  maded with love <3 by blackout314 @ ghlab
  -------------------------------------------
"""


if len(sys.argv) > 1:
  uid = sys.argv[1]
  url = "https://bitcointalk.org/index.php?action=profile;u=" + uid + ";sa=statPanel"
  page = requests.get(url)
  tree = html.fromstring(page.content)

  online = tree.xpath("//td[@class='windowbg2'][1]/table[1]/tr/td[2]/text()")
  print '[DATA]'
  for d in online:
    print ' >', d

  boards = tree.xpath("//td[@class='windowbg2'][2]/table/tr/td/a/text()")
  boards_perc = tree.xpath("//td[@class='windowbg2'][2]/table/tr/td/text()")
  print '[BOARDS]'
  for i in range(len(boards)):
    print ' +', boards_perc[i], "", boards[i]

  pboards = tree.xpath("//td[@class='windowbg2'][1]/table/tr/td/a/text()")
  pboards_perc = tree.xpath("//div[@id='bodyarea']/table/tr/td/table/tr[6]/td[@class='windowbg2'][1]/table/tr/td/text()")
  print '[BOARDS]'
  for i in range(len(pboards)):
    print ' +', pboards_perc[i], "", pboards[i]
else:
  print """
  usage: python btctalk.py {UID}
  """

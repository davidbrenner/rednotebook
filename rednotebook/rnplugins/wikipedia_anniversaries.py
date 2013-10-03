#!/usr/bin/python2
"""
Grab the current day's selected anniversaries
"""

from rednotebook.plugins import RedNotebookPlugin
import BeautifulSoup
import urllib2
import re
import datetime

class WikiAnniversaries(RedNotebookPlugin):
    def get_text(self):
        """ Returns text to be inserted """
        today = self.day
        month = today.strftime("%B")
        day = str(today.day)
        mon_day_str = month + ' ' + day
        site = 'http://en.wikipedia.org/wiki/Wikipedia:Selected_anniversaries/' + \
                month + '_' + day
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(site,headers=hdr)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup.BeautifulSoup(page)

        cur = soup.find("a")
        found = False
        count = 0
        while not found:
            if cur and cur.string:
                if mon_day_str == cur.string:
                    if count == 1:
                        found = True
                        break
                    count += 1
            cur = cur.findNext("a")

        # clean up html and convert to markdown
        anniversaries = str(cur.findNext("ul"))
        anniversaries = re.sub(r'class=".*?"',r'',anniversaries)
        anniversaries = re.sub(r'<a href="(.*?)" title=".*?">(.*?)</a>',
                r'[\2](http://en.wikipedia.org\1)',anniversaries)
        anniversaries = re.sub(r'<li>(.*?)</li>',r'* \1',anniversaries)
        anniversaries = re.sub(r'<i>(.*?)</i>',r'*\1*',anniversaries)
        anniversaries = re.sub(r'<b>(.*?)</b>',r'**\1**',anniversaries)
        anniversaries = re.sub(r'<ul>',r'',anniversaries)
        anniversaries = re.sub(r'</ul>',r'',anniversaries)
        return anniversaries

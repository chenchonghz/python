__author__ = 'Steve'

import urllib2
import re



class http:

    def __init__(self, uri = 'http://www.ffdy.cc/?z'):
        self.uri = uri
        self.list = []
        self.member = -1

    def show(self, uri = ""):


        if uri != '':
            self.uri = uri
        print self.uri
        con = urllib2.urlopen(self.uri).read()


        reg = re.compile(r'<\s*[Aa]{1}\s+[^>]*?[Hh][Rr][Ee][Ff]\s*=\s*["\']?[^>]+?["\']?.*?>')
        http = re.compile(r'[Hh][Rr][Ee][Ff]\s*=\s*[\'\"](.*?)[\'\"]')
        m = re.findall(reg, con)

        for i in m:
            l = re.findall(http, i)
            #print '[Get]', l[0]
            if l[0] != '#' and l[0] != '/' and l[0][0:4] == 'http':
                self.list.append(l[0])
                print '[Handle]', l[0]

            if l[0] == '#' or l[0] == '/' or l[0][0:4] != 'http':
                print '[Abandon]', l[0]

        self.member += 1
        print self.member
        self.show(self.list[self.member])

httper = http()


try:
    httper.show("http://www.baidu.com/s?tn=baiduhome_pg&ie=utf-8&bs=python+%E6%8A%9B%E5%87%BA%E5%BC%82%E5%B8%B8%E7%BB%A7%E7%BB%AD%E8%BF%90%E8%A1%8C&f=8&rsv_bp=1&rsv_spt=1&wd=python+%E6%8A%9B%E5%87%BA%E5%BC%82%E5%B8%B8%E6%88%96%E9%94%99%E8%AF%AF%E5%90%8E%E7%BB%A7%E7%BB%AD%E8%BF%90%E8%A1%8C&rsv_sug3=11&rsv_sug4=640&rsv_sug1=8&rsv_sug=1&inputT=4639")
    raise Exception('Oh no!')
except Exception, e:
    print 'error: %s' % e

#httper.show("http://www.baidu.com/s?tn=baiduhome_pg&ie=utf-8&bs=%E5%9C%A8google+app+engine%E4%B8%AD%E5%BB%BAphp%E7%BD%91%E7%AB%99&f=8&rsv_bp=1&rsv_spt=1&wd=%E5%9C%A8google+app+engine%E9%83%A8%E7%BD%B2%E8%87%AA%E5%8A%A8%E8%BF%90%E8%A1%8C%E7%9A%84python%E7%A8%8B%E5%BA%8F&rsv_sug3=31&rsv_sug4=12047&rsv_sug1=17&inputT=9376")
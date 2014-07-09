import os
from zope.interface import Interface, implements
from w3lib.url import file_uri_to_path
from scrapy.contrib.feedexport import IFeedStorage

#Custom file feed storage that overwrites file
class OverwriteFileFeedStorage(object):

    implements(IFeedStorage)

    def __init__(self, uri):
        self.path = file_uri_to_path(uri)

    def open(self, spider):
        dirname = os.path.dirname(self.path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        return open(self.path, 'wb')

    def store(self, file):
        file.close()

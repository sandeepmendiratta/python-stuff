class Site():
    prefix = "https://"
    def __init__(self,url):
        self.url = url
    def fullname(self):
        # return ("{}{}".format(self.prefix, self.url))
        return (f'{self.prefix}{self.url}')
name1 = Site("hello.com")
print(name1.fullname())

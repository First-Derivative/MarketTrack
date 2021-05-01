
class ScrapingError(Exception):
  ''' 
  Abstract Error Class
  '''
  pass

class ItemNotFound(ScrapingError):
  def __init__(self, platform):
    self.message = "Searched Item was not found on platform: {}".format(platform)
    super().__init__(self.message)

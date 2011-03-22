try:
    import json
except ImportError:
    import simplejson as json 
import restkit

HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'text/plain',
}        

class MDB(object):
    
    def __init__(self, baseuri):
        self._uri = baseuri
                
    @property
    def _resource(self):        
        return restkit.Resource(self._uri)
    
    def search(self, term):
        """searches mdb with term.
        
        returns a list of records. 
        each record is similar to the record returned at ``info`` call 
        """         
        path = 'search/%s' % term
        response = self._resource.get(path=path, headers=HEADERS)
        return json.loads(response.body)
    
    def access(self, uid, revid=None):
        """
        allowed: Boolean - access allowed (general, without dates in context)
        message: String: reason
        """        
        path = 'access/%s' % uid
        if revid:
            path = '%s/%s' % path, revid
        response = self._resource.get(path=path, headers=HEADERS)
        return json.loads(response.body)
    
    def info(self, uid, revid=None):
        """information about one item in the store. It is a dict with
        attributes::

            title: String
            description 
            repository: String
            uid: String (base62)
            revision (dict):
                revid: String
                title: String
                description: String
                mimetype: String
                filename: String
                size: int
                alttag: String                            
        """
        path = 'info/%s' % uid
        if revid:
            path = '%s/%s' % path, revid
        response = self._resource.get(path=path, headers=HEADERS)
        return json.loads(response.body)
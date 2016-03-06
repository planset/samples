import base64
import urllib
import urllib2
try:
    import json
except:
    import simplejson as json

class NotAuthorizedTokenException(Exception):
    pass

class Facebook(object):
    access_token = None
    expires = None
    FB_URL_OAUTH = "https://www.facebook.com/dialog/oauth?client_id={client_id}&redirect_uri={redirect_uri}"
    FB_URL_LOGOUT = "https://www.facebook.com/logout.php?next={redirect_uri}&access_token={access_token}"
    FB_URL_GRAPH_API = "https://graph.facebook.com"
    profile = None
    
    def __init__(self, app_id, app_secret, redirect_uri, scope=None, access_token=None):
        self.app_id = app_id
        self.app_secret = app_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.set_token(access_token)
        
    def set_token(self, access_token):
        self.access_token = access_token
                
    def is_authorized(self):
        """
        TODO: check expire?
        """
        return not (self.access_token is None)

    def oauth_login_url(self, redirect_uri=None, preserve_path=True):
        if not redirect_uri:
            redirect_uri = self.redirect_uri
        fb_login_uri = self.FB_URL_OAUTH.format(
                         client_id=self.app_id, 
                         redirect_uri=redirect_uri)

        if self.scope:
            fb_login_uri += "&scope=%s" % ",".join(self.scope)
        return fb_login_uri
    
    def logout_url(self, redirect_uri=None):
        if not redirect_uri:
            redirect_uri = self.redirect_uri
        fb_logout_uri = self.FB_URL_LOGOUT.format(
                         access_token=self.access_token, 
                         redirect_uri=redirect_uri)
        return fb_logout_uri

    def fbapi_auth(self, code):
        params = {'client_id': self.app_id,
                  'redirect_uri': self.redirect_uri,
                  'client_secret': self.app_secret,
                  'code': code}

        result = self._fbapi_get_string(path=u"/oauth/access_token?", params=params,
                                  encode_func=self._simple_dict_serialisation)
        pairs = result.split("&", 1)
        result_dict = {}
        for pair in pairs:
            (key, value) = pair.split("=")
            result_dict[key] = value
        
        self.access_token = result_dict["access_token"]
        self.expires = result_dict["expires"]
        return (result_dict["access_token"], result_dict["expires"])


    def fbapi_get_application_access_token(self, id):
        token = fbapi_get_string(
            path=u"/oauth/access_token",
            params=dict(grant_type=u'client_credentials', client_id=id,
                        client_secret=self.app_secret),
            domain=u'graph')

        token = token.split('=')[-1]
        if not str(id) in token:
            print 'Token mismatch: %s not in %s' % (id, token)
        return token


    def fql(self, fql, token, args=None):
        if not args:
            args = {}

        args["query"], args["format"], args["access_token"] = fql, "json", token
        return json.loads(
            urllib2.urlopen("https://api.facebook.com/method/fql.query?" +
                            urllib.urlencode(args)).read())

                            
    def me(self):
        return self._call_graph_api("/me")

    def me_friends(self):
        return self._call_graph_api("/me/friends")

    def me_notes(self):
        return self._call_graph_api("/me/notes")

    def get_note(self, id):
        return self._call_graph_api("/" + str(id))

    def save_note(self, id, subject, message):
        path = "/" + str(id) if id else "/me/notes"
        postdata = {"access_token":self.access_token,"subject": subject, "message": message}
        result = self._fbapi_post_string(path, params=postdata)
        return
    
    def fb_call(self, call, args=None):
        return json.loads(urllib2.urlopen("https://graph.facebook.com/" + call +
                                          '?' + urllib.urlencode(args)).read())

    def _simple_dict_serialisation(self, params):
        return "&".join(map(lambda k: "%s=%s" % (k, params[k]), params.keys()))

    def _fbapi_post_string(self, path, domain=u'graph', params={}, 
                          access_token=None,
                          encode_func=urllib.urlencode):
        if access_token:
            params[u'access_token'] = access_token

        for k, v in params.iteritems():
            if hasattr(v, 'encode'):
                params[k] = v.encode('utf-8')

        url = u'https://' + domain + u'.facebook.com' + path
        params_encoded = encode_func(params)
        try:
            result = urllib.urlopen(url, params_encoded).read()
        except urllib2.HTTPError, e:
            if e.code == 400:
                result = e.read()

        return result

    def _fbapi_get_string(self, path, domain=u'graph', params=None, 
                          access_token=None,
                          encode_func=urllib.urlencode):
        """Make an API call"""
        if not params:
            params = {}
        params[u'method'] = u'GET'
        if access_token:
            params[u'access_token'] = access_token

        for k, v in params.iteritems():
            if hasattr(v, 'encode'):
                params[k] = v.encode('utf-8')

        url = u'https://' + domain + u'.facebook.com' + path
        params_encoded = encode_func(params)
        url = url + params_encoded
        try:
            result = urllib2.urlopen(url).read()
        except urllib2.HTTPError, e:
            if e.code == 400:
                result = e.read()

        return result

    def _call_graph_api(self, path, params={}, limit=5000, offset=0):
        """
        call_graph_api("/me")
        call_graph_api("/me/friends")
        """
        if not self.access_token:
            raise Exception("not authorized")

        result = self._fbapi_get_string(path=path+"?", 
                                      domain=u'graph',
                                      params=params,
                                      access_token=self.access_token,
                                      encode_func=self._simple_dict_serialisation)
        return json.loads(result)

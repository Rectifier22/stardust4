import os
import jinja2
import webapp2
import cgi
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
from content import COURSES

template_dir = os.path.join(os.path.dirname(__file__), 'html_templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, courses=COURSES, **kw))    

class MainPage(Handler):
    def get(self):
        self.render("/main_page.html", page_name="home")

class NotesHandler(Handler):
    def get(self):
        self.render('notes.html', page_name="notes")

class CourseHandler(Handler):
    def get(self, course_number):
        self.render('course.html', course_number=int(course_number), course=COURSES[int(course_number)-1], page_name="notes")

DEFAULT_WALL = 'Public'

def wall_key(wall_name=DEFAULT_WALL):
  """Constructs a Datastore key for a Wall entity.

  We use wall_name as the key.
  """
  return ndb.Key('Wall', wall_name)

class Author(ndb.Model):
  """Sub model for representing an author."""
  identity = ndb.StringProperty(indexed=True)
  name = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)

class Post(ndb.Model):
  """A main model for representing an individual post entry."""
  author = ndb.StructuredProperty(Author)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)


class CommentsHandler(Handler):
  def get(self, **kwargs):
    wall_name = self.request.get('wall_name',DEFAULT_WALL)
    if wall_name == DEFAULT_WALL.lower(): wall_name = DEFAULT_WALL

    posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)

    posts =  posts_query.fetch()

    user = users.get_current_user()
    if user:
        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'
        user_name = user.nickname()
    else:
        url = users.create_login_url(self.request.uri)
        url_linktext = 'Login'
        user_name = 'Anonymous Poster'

    posts_html = ''
    for post in posts:

      if user and user.user_id() == post.author.identity:
        posts_html += '<div><h3>(You) ' + post.author.name + '</h3>\n'
      else: 
        posts_html += '<div><h3>' + post.author.name + '</h3>\n'

      posts_html += 'wrote: <blockquote>' + cgi.escape(post.content) + '</blockquote>\n'
      posts_html += '</div>\n'

    sign_query_params = urllib.urlencode({'wall_name': wall_name})

    self.render('comments.html', page_name="comments",  sqp=sign_query_params, wallname=cgi.escape(wall_name), 
                                    username=user_name, url=url, urllinktext=url_linktext, postshtml=posts_html, **kwargs)  
   
  def post(self):

      wall_name = self.request.get('wall_name',DEFAULT_WALL)
      post = Post(parent=wall_key(wall_name))

      if users.get_current_user():
        post.author = Author(
              identity=users.get_current_user().user_id(),
              name=users.get_current_user().nickname(),
              email=users.get_current_user().email())
      else:
        post.author = Author(
              name='anonymous@anonymous.com',
              email='anonymous@anonymous.com')

      post.content = self.request.get('content')
  
      query_params = {"comment": post.content}

      is_valid, errors = validate_comment(post)
      if is_valid:
        post.put()
        self.redirect('/comments.html?wall_name=' + wall_name)
      else:
        for k, v in errors.items():
          query_params[k] = v
        self.get(**query_params)

def validate_comment(post):
  valid = True
  errors = {}
  if len(post.content) < 1:
    errors['comment_error'] = "Please enter a comment to display."
    valid = False
  return valid, errors
    
app = webapp2.WSGIApplication([
    ('/*', MainPage),
    ('/notes.html', NotesHandler), 
    (r'/course/(\d+)/', CourseHandler), 
    ('/comments.html', CommentsHandler),
    ('/sign', CommentsHandler)
], debug=True)

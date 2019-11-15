from webapp import app, db, DataProcessing
from webapp.models import User, Post



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'app': app, 'DataProcessing': DataProcessing}

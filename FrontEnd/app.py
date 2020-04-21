from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///modules.db'
db=SQLAlchemy(app)

class BlogModule(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100),nullable=False)
    staff = db.Column(db.Text, nullable =False)
    project = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)

def __repr__(self):
    return 'BlogModule' + str(self.id)

all_modules=[
    {
      'title' : 'Cloud Computing',
      'staff':'Sukhpal & Joseph',
      'project': 'Mini Project'
    },
    {
        'title': 'Data Analytics',
        'staff':'Bhusan & Anthony',
        'project' : 'Coursework'
    },
   {
        'title': 'Deep Learning',
        'staff':'Sean Gong',
        'project' : 'Course work'
    },
   {
        'title': 'Digital Media',
        'staff':'Laurissa'
   }
]
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/modules', methods=['GET','POST'])
def modules():
    if request.method == 'POST':
        post_title = request.form['title']
        post_staff = request.form['staff']
        post_project = request.form['project']
        new_post = BlogModule(title=post_title, staff=post_staff, project=post_project)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/modules')
    else:
        all_modules=BlogModule.query.order_by(BlogModule.date_posted).all()
        return render_template('modules.html', modules=all_modules)

@app.route('/modules/delete/<int:id>')
def delete(id):
    post = BlogModule.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/modules')

@app.route('/modules/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    post = BlogModule.query.get_or_404(id)
    if request.method=='POST':
        post.title = request.form['title']
        post.staff = request.form['staff']
        post.project = request.form['project']
        db.session.commit()
        return redirect('/modules')
    else:
        return render_template('edit.html',post=post)

if __name__ == "__main__":
    app.run(debug=True)



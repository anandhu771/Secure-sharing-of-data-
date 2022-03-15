from flask import Flask,render_template,request,redirect
from db_connection import Db
import random,datetime
app = Flask(__name__)


@app.route('/',methods=['get','post'])
def login():
    if request.method == 'POST':
        db = Db()
        username=request.form['textfield']
        password=request.form['textfield2']
        ss = db.selectOne("select * from login where username = '"+username+"' and password = '"+password+"'")
        if ss is not None:
            if ss['user_type'] == 'admin':
                return redirect('/admin_home')
            elif ss['user_type'] == 'minister':
                return redirect('/minister')
            else :
                return redirect('/officer')

    return render_template('login.html')


@app.route('/add_department',methods=['get','post'])
def add_department():
    if request.method == 'POST':
        dept=request.form['textfield']
        db = Db()
        db.insert("insert into department values ('','"+dept+"')")
        return '<script>alert("department added");window.location="/add_department"</script>'
    return render_template('Admin/add_department.html')


@app.route('/minister_registration',methods=['get','post'])
def minister_registration():
    if request.method == 'POST':
        name = request.form['textfield']
        gender = request.form['radio']
        email = request.form['textfield3']
        district = request.form['select']
        proof = request.files['fileField2']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        proof.save(r"C:\Users\BEST\PycharmProjects\secure sharing of data\static\minister\\"+date+'.jpg')
        proof1 = "/static/minister/"+date+'.jpg'
        photo = request.files['fileField']
        photo.save(r"C:\Users\BEST\PycharmProjects\secure sharing of data\static\photo\\"+date+'.jpg')
        photo1 = "/static/photo/"+date+'.jpg'
        contact_number = request.form['textfield5']
        place = request.form['textfield6']
        pas = random.randint(00000,99999)
        db = Db()
        ss = db.insert("insert into login values ('','"+email+"','"+str(pas)+"','minister')")
        db.insert("insert into minister values ('"+str(ss)+"','"+name+"','"+proof1+"','"+place+"','"+email+"','"+photo1+"','"+contact_number+"','"+district+"','"+gender+"')")
        return '<script>alert("minister added");window.location="/minister_registration"</script>'

    return render_template('Admin/minister_Registration_form.html')

@app.route('/view_minister')
def view_minister():
    db=Db()
    res =db.select("select * from minister")
    return render_template('Admin/view_minister.html',data=res)

@app.route('/officer_registration',methods=['get','post'])
def officer_registration():
    if request.method == 'POST':
        name = request.form['textfield']
        gender = request.form['radio']
        email = request.form['textfield3']
        district = request.form['select']
        proof = request.files['fileField2']
        date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        proof.save(r"C:\Users\BEST\PycharmProjects\secure sharing of data\static\officer//"+date+'.jpg')
        proof1 = "/static/officer/"+date+'.jpg'
        photo = request.files['fileField']
        photo.save(r"C:\Users\BEST\PycharmProjects\secure sharing of data\static\photo//"+date+'.jpg')
        photo1 = "/static/photo/"+date+'.jpg'
        contact_number = request.form['textfield5']
        place = request.form['textfield6']
        pas = random.randint(00000,99999)
        db =Db()
        ss = db.insert("insert into login values('','"+email+"','"+str(pas)+"','officer')")
        db.insert("insert into officer values ('"+str(ss)+"','"+name+"','"+email+"','"+contact_number+"','"+proof1+"','"+photo1+"','"+district+"','"+place+"','"+gender+"')")
        return '<script>alert("officer added");window.location="/officer_registration"</script>'

    return render_template('Admin/officer_registration_form.html')

@app.route('/view_officer')
def view_officer():
    db = Db()
    res = db.select("select * from officer" )
    print(res)
    return render_template('Admin/view_officer.html',data=res)

@app.route('/admin_home')
def admin_home():
    return render_template('Admin/admin_home.html')


@app.route('/allocate_minister/<m_id>',methods=['get','post'])
def allocate_minister(m_id):
    if request.method == 'POST':

        department=request.form['select']
        year =request.form['textfield5']
        db=Db()
        db.insert("insert into allocate_minister VALUES ('','"+department+"','"+m_id+"','"+year+"')")
        return '''<script>alert("allocated successfully");window.location="/view_minister"</script>'''
    else:
        db=Db()
        res=db.select("select * from department ")
        return render_template('Admin/allocate_minister.html',data=res)

@app.route('/allocate_officer',methods=['get','post'])
def allocate_officer():
    if request.method == 'POST':
        department=request.form['select']
    return render_template('Admin/allocate_officer.html')

@app.route('/view_suggestions')
def view_suggestions():
    db = Db()
    res = db.select("SELECT * FROM minister,suggestions WHERE minister.minister_id = suggestions.minister_id")
    return render_template('Admin/view_suggestions.html',data=res)

@app.route('/view_complaint')
def view_complaint():
    db = Db()
    res = db.select("SELECT * FROM officer,complaint WHERE officer.officer_id = complaint.sender_id and complaint.complaint_reply='pending'")
    res1 = db.select("SELECT * FROM minister,complaint WHERE minister.minister_id = complaint.complaint_id and complaint.complaint_reply='pending'")
    return render_template('Admin/view_complaint.html', data=res, data1=res1)


@app.route('/send_reply/<c_id>',methods=['get','post'])
def send_reply(c_id):

    if request.method == 'POST':

        reply = request.form['textarea']
        db=Db()
        db.update("update complaint set complaint_reply='"+reply+"',reply_date=curdate() where complaint_id='"+c_id+"'")
        return '''<script>alert("reply sent ");window.location="/view_complaint"</script>'''
    else:

        return render_template('Admin/send_reply.html')




if __name__ == '__main__':
    app.run()

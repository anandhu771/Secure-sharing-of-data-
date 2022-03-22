from flask import Flask,render_template,request,redirect,session
from db_connection import Db
import random,datetime
app = Flask(__name__)
app.secret_key = "123"


@app.route('/',methods=['get','post'])
def login():
    if request.method == 'POST':
        db = Db()
        username=request.form['textfield']
        password=request.form['textfield2']
        ss = db.selectOne("select * from login where username = '"+username+"' and password = '"+password+"'")
        if ss is not None:
            if ss['user_type'] == 'admin':
                session['lg']='lin'
                return redirect('/admin_home')
            elif ss['user_type'] == 'minister':
                session['lg'] = 'lin'
                session['m_id'] = ss['login_id']
                return redirect('/minister')
            else :
                session['lg'] = 'lin'
                session['o_id'] = ss['login_id']
                return redirect('/officer')

    return render_template('login1.html')
@app.route('/logout')
def logout():
    session.clear()
    session['lg']=""
    return redirect('/')


@app.route('/add_department',methods=['get','post'])
def add_department():
    if session['lg'] == "lin":
        if request.method == 'POST':
            dept=request.form['textfield']
            db = Db()
            db.insert("insert into department values ('','"+dept+"')")
            return '<script>alert("department added");window.location="/add_department"</script>'
        return render_template('Admin/add_department.html')
    else:
        return redirect('/')

@app.route('/minister_registration',methods=['get','post'])
def minister_registration():
    if session['lg'] == "lin":
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
    else:
        return redirect('/')
@app.route('/view_minister')
def view_minister():
    if session['lg'] == "lin":
        db=Db()
        res =db.select("select * from minister")
        return render_template('Admin/view_minister.html',data=res)
    else:
        return redirect('/')


@app.route('/officer_registration',methods=['get','post'])
def officer_registration():
    if session['lg'] == "lin":
        if request.method == 'POST':
            name = request.form['textfield']
            gender = request.form['radio']
            email = request.form['textfield3']
            district = request.form['select']
            proof = request.files['fileField2']
            date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
            proof.save(r"C:\Users\BEST\PycharmProjects\secure sharing of data\static\officer\\"+date+'.jpg')
            proof1 = "/static/officer/"+date+'.jpg'
            photo = request.files['fileField']
            photo.save(r"C:\Users\BEST\PycharmProjects\secure sharing of data\static\photo\\"+date+'.jpg')
            photo1 = "/static/photo/"+date+'.jpg'
            contact_number = request.form['textfield5']
            place = request.form['textfield6']
            pas = random.randint(00000,99999)
            db =Db()
            ss = db.insert("insert into login values('','"+email+"','"+str(pas)+"','officer')")
            db.insert("insert into officer values ('"+str(ss)+"','"+name+"','"+email+"','"+contact_number+"','"+proof1+"','"+photo1+"','"+district+"','"+place+"','"+gender+"')")
            return '<script>alert("officer added");window.location="/officer_registration"</script>'

        return render_template('Admin/officer_registration_form.html')
    else:
        return redirect('/')

@app.route('/view_officer')
def view_officer():
    if session['lg'] == "lin":
        db = Db()
        res = db.select("select * from officer" )
        print(res)
        return render_template('Admin/view_officer.html',data=res)
    else:
        return redirect('/')

@app.route('/admin_home')
def admin_home():
    if session['lg'] == "lin":
        return render_template('Admin/admin_home.html')
    else:
        return redirect('/')

@app.route('/allocate_minister/<m_id>',methods=['get','post'])
def allocate_minister(m_id):
    if session['lg'] == "lin":
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
    else:
        return redirect('/')


@app.route('/allocate_officer/<o_id>',methods=['get','post'])
def allocate_officer(o_id):
    if session['lg'] == "lin":
        if request.method == 'POST':
            department=request.form['select']
            db=Db()
            db.insert("insert into allocate_officer VALUES ('','"+o_id+"','"+department+"')")
            return '''<script>alert("officer allocated successfully");window.location="/view_officer"</script>'''
        else:
            db=Db()
            res=db.select("select * from department")
            return render_template('Admin/allocate_officer.html',data=res )
    else:
        return redirect('/')

@app.route('/view_suggestions')
def view_suggestions():
    if session['lg'] == "lin":
        db = Db()
        res = db.select("SELECT * FROM minister,suggestions WHERE minister.minister_id = suggestions.minister_id")
        return render_template('Admin/view_suggestions.html',data=res)
    else:
        return redirect('/')

@app.route('/view_complaint')
def view_complaint():
    if session['lg'] == "lin":
        db = Db()
        res = db.select("SELECT * FROM officer,complaint WHERE officer.officer_id = complaint.sender_id and complaint.complaint_reply='pending'")
        res1 = db.select("SELECT * FROM minister,complaint WHERE minister.minister_id = complaint.complaint_id and complaint.complaint_reply='pending'")
        return render_template('Admin/view_complaint.html', data=res, data1=res1)
    else:
        return redirect('/')

@app.route('/send_reply/<c_id>',methods=['get','post'])
def send_reply(c_id):
    if session['lg'] == "lin":

        if request.method == 'POST':

            reply = request.form['textarea']
            db=Db()
            db.update("update complaint set complaint_reply='"+reply+"',reply_date=curdate() where complaint_id='"+c_id+"'")
            return '''<script>alert("reply sent ");window.location="/view_complaint"</script>'''
        else:

            return render_template('Admin/send_reply.html')
    else:
        return redirect('/')

# ------Minister------
@app.route('/minister')
def minister_home():
    if session['lg'] == "lin":
        return render_template('minister/minister_home.html')
    else:
        return redirect('/')

@app.route('/minister_profile')
def minister_profile():
    if session['lg'] == "lin":
        db=Db()
        res= db.selectOne("select * from minister,allocate_minister,department where minister.minister_id = allocate_minister.minister_id and department.dept_id=allocate_minister.dept_id and minister.minister_id = '"+str(session['m_id'])+"' ")
        return render_template('minister/minister_profile.html',data=res)
    else:
        return redirect('/')

@app.route('/minister_officer_view')
def minister_officer_view():
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from allocate_officer,allocate_minister,officer where allocate_officer.department_id = allocate_minister.dept_id and allocate_officer.officer_id = officer.officer_id and allocate_minister.minister_id = '"+str(session['m_id'])+"'")
        return render_template('minister/minister_officer_view.html',data=res)
    else:
        return redirect('/')
@app.route('/inbox_from_officer')
def inbox_from_officer():
    if session['lg'] == "lin":
        db=Db()
        res = db.select("select * from allocate_officer,allocate_minister,document,officer where allocate_officer.department_id = allocate_minister.dept_id and allocate_officer.allocate_officer_id = document.allocate_officer_id and allocate_minister.minister_id = '"+str(session['m_id'])+"'and allocate_officer.officer_id = officer.officer_id")
        return render_template('minister/inbox_from_officer.html',data=res)
    else:
        return redirect('/')
@app.route('/minister_send_suggestions',methods=['get','post'])
def minister_send_suggestion():
    if session['lg'] == "lin":
        if request.method == "POST":
           res = request.form['textarea']
           db=Db()
           db.insert("insert into suggestions VALUES('','"+str(session['m_id'])+"',curdate(),'"+res+"') ")
           return '''<script>alert("suggestion sent");window.location = "/minister_send_suggestions"</script>'''
        return render_template('minister/minister_send_suggestions.html')
    else:
        return redirect('/')
#---------------Officer----------------

@app.route('/officer')
def officer_home():
    if session['lg'] == "lin":
        return render_template('officer/officer_home.html')
    else:
        return redirect('/')
@app.route('/officer_profile')
def officer_profile():
    if session['lg'] == "lin":
        db = Db()
        res = db.selectOne("select * from officer,allocate_officer,department where officer.officer_id = allocate_officer.officer_id and department.dept_id=allocate_officer.department_id and officer.officer_id = '" + str(session['o_id']) + "' ")
        return render_template('officer/officer_profile.html',data=res)
    else:
        return redirect('/')

@app.route('/importent_document_to_minister',methods=['get','post'])
def officer_importent_document_to_minister():

    if session['lg'] == "lin":
        if request.method == 'POST':

            db=Db()
            res = request.files['fileField']
            type = request.form['textfield6']
            date = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
            res.save(r"C:\Users\BEST\PycharmProjects\secure sharing of data\static\documents\\" + date + '.pdf')
            proof1 = "/static/documents/" + date + '.pdf'
            ss = db.selectOne("select * from allocate_officer where officer_id = '"+str(session['o_id'])+"'")
            oid = ss['allocate_officer_id']
            print (oid,ss)
            db.insert("insert into document VALUES ('','"+str(oid)+"','"+proof1+"','"+type+"',curdate())")
            return '''<script>alert("Document Sent");window.location="/importent_document_to_minister"</script>'''
        return render_template('officer/importent_document_to_minister.html')
    else:
        return redirect('/')

@app.route('/officer_send_complaint',methods=['get','post'])
def officer_send_complaint():
    if session['lg'] == "lin":
        if request.method == 'POST':
            res=request.form['textarea']
            db=Db()
            db.insert("insert into complaint VALUES ('','"+str(session['o_id'])+"','"+res+"',curdate(),'pending','pending')")
            return '''<script>alert("complaint Sent");window.location="/officer_send_complaint"</script>'''

        return render_template('officer/officer_send_complaint.html')
    else:
        return redirect('/')

@app.route('/officer_view_complaint_reply')
def officer_view_complaint_reply():
    if session['lg'] == "lin":
        db=Db()
        res=db.select("select * from complaint where sender_id ='"+str(session['o_id'])+"'")
        return render_template('officer/officer_view_complaint_reply.html',data=res)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(port=4000)

from flask import Flask,render_template,request,redirect,session,jsonify,send_file
from db_connection import Db
import random,datetime
import demjson
import numpy as np
import qrcode
import pyAesCrypt
from aesnew import AESCipher
from asw_img_encr import IMG_xor,re_size
from functools import partial
from des import DesKey


app = Flask(__name__)
app.secret_key = "123"
staticpath=r"C:\Users\BEST\PycharmProjects\secure sharing of data\static\\"

@app.route('/')
def entry_page():
    return render_template('index.html')

@app.route('/login',methods=['get','post'])
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
@app.route('/login1')
def login1():
    return render_template("login.html")
@app.route('/login_post',methods=["get"])
def loginpost():
    username=request.args.get("uname")
    qry="select imei,officer_id as userid from officer where officer_email='"+username+"'"
    print(qry)
    db=Db()
    result=db.selectOne(qry)
    if result is not None:
        #
        # random_number=random.randint(0000000000000000,9999999999999999)
        imei_number=str(result['imei'])+str(0)
        userid=result['userid']
        session['lid']=userid
        session['login'] = 'login'
        session['lg'] = 'lin'
        session['o_id'] = userid
        # print("before encryption",random_number)



        listtt = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        print(type(listtt))
        print(listtt)
        np.random.shuffle(listtt)
        print(listtt)
        string=""
        key=""
        for i in listtt:
            string=string+str(i)+"#"
            key=key+str(i)


        print("string",string)
        session["string"]=key
        print("key",key)
        cipher = AESCipher(str(imei_number))
        encrypted = cipher.encrypt(str(string))
        print("encrypted",encrypted )
        #
        decrypted = cipher.decrypt(encrypted)
        #
        print("decrypted",decrypted)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4, )
        qr.add_data(str(encrypted))
        qr.make(fit=True)
        img = qr.make_image()
        print("width",img.width)
        # print("length",img.)
        sring1=str(encrypted)
        sring1=sring1.replace('/','9')
        sring1=sring1.replace('\\','3')
        sring1 = sring1.replace('.', '0')

        img.save(staticpath+"qr\\" + sring1 + ".jpg")
        imgpath = "/static/qr/" + sring1 + ".jpg"

        # decrypted = cipher.decrypt(encrypted)
        # print("encrypted=", encrypted)
        # print("decrypted", decrypted.decode('utf-8'))
        return jsonify(imgpath)
    else:
        status="No user"
        return jsonify(status)

@app.route('/cheching',methods=["post"])
def check():
    print("lll")
    c=request.form["a"]
    print(c)
    string=session["string"]
    k=c.split(',')

    tot=0;
    c=1;

    for i in k:
        if str(i)!="":
            print(string[(int(i) - 1)], c)
            if string[(int(i) - 1)] == str(c):
                tot = tot + 1
            else:
                tot = 0
            c = c + 1


    print(tot,"kkkkkkkk")
    op="no"

    if tot==5:
        op="ok"

    print(k)
    print(string,"aaaa")
    print(string)
    return jsonify(op)

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
            imei= request.form['textfield7']
            pas = random.randint(00000,99999)
            db =Db()
            ss = db.insert("insert into login values('','"+email+"','"+str(pas)+"','officer')")
            db.insert("insert into officer values ('"+str(ss)+"','"+name+"','"+email+"','"+contact_number+"','"+proof1+"','"+photo1+"','"+district+"','"+place+"','"+gender+"','"+imei+"')")
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
        return render_template('Admin/index.html')
    else:
        return redirect('/')

@app.route('/allocate_minister/<m_id>',methods=['get','post'])
def allocate_minister(m_id):
    if session['lg'] == "lin":
        if request.method == 'POST':

            department=request.form['select']
            year =request.form['textfield5']
            db=Db()
            ss = db.selectOne("select * from allocate_minister where minister_id = '"+m_id+"' and dept_id = '"+department+"'")
            if ss is None:
                db.insert("insert into allocate_minister VALUES ('','"+department+"','"+m_id+"','"+year+"')")

                return '''<script>alert("allocated successfully");window.location="/view_minister"</script>'''
            else:
                return '''<script>alert("already allocated");window.location="/view_minister"</script>'''
        else:
            db=Db()
            res=db.select("select * from department ")
            return render_template('Admin/allocate_minister.html',data=res)
    else:
        return redirect('/')

@app.route('/delete_minister/<d_id>')
def delete_minister(d_id):
    db=Db()
    db.delete("delete from minister where minister_id = '"+d_id+"'")
    db.delete("delete from login where login_id = '"+d_id+"'")
    return '''<script>alert("Minister Deleted");window.location="/view_minister"</script>'''

@app.route('/delete_officer/<d_id>')
def delete_officer(d_id):
    db=Db()
    db.delete("delete from officer where officer_id = '"+d_id+"'")
    db.delete("delete from login where login_id = '" + d_id + "'")
    return '''<script>alert("Officer Deleted");window.location="/view_officer"</script>'''

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
        res = db.select("SELECT * FROM minister,suggestions WHERE minister.minister_id = suggestions.minister_id and suggestions.reply = 'pending'")
        return render_template('Admin/view_suggestions.html',data=res)
    else:
        return redirect('/')

@app.route('/view_complaint')
def view_complaint():
    if session['lg'] == "lin":
        db = Db()
        res = db.select("SELECT * FROM officer,complaint WHERE officer.officer_id = complaint.sender_id and complaint.complaint_reply='pending'")
        res1 = db.select("SELECT * FROM minister,complaint WHERE minister.minister_id = complaint.sender_id and complaint.complaint_reply='pending'")
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

@app.route('/admin_sug_reply/<s_id>',methods=['get','post'])
def sug_reply(s_id):
    if request.method == 'POST':
        reply = request.form['textarea']
        db = Db()
        db.update(
            "update suggestions set reply='" + reply + "',reply_date=curdate() where suggestion_id='" + s_id + "'")
        return '''<script>alert("reply sent ");window.location="/view_suggestions"</script>'''
    else:
        return render_template('Admin/admin_sug_reply.html')
@app.route('/add_group',methods=['get','post'])
def group():
    if request.method == 'POST':
        group = request.form['textfield']
        pasword = random.randint(00000, 99999)
        db=Db()
        ss=db.selectOne("select * from group1 where group_name='"+group+"'")
        if ss is not None:
            return  '''<script>alert("Group already added");window.location="/add_group"</script>'''
        else:
            db.insert("insert into group1 VALUES ('','"+group+"','"+str(pasword)+"')")
        return '''<script>alert("Group Created");window.location="/add_group"</script>'''
    else:
       return render_template('Admin/Group.html')

@app.route('/group_view')
def group_view():

    db = Db()
    res= db.select("select * from group1")
    return render_template('Admin/group_view.html',data=res)
@app.route('/ring_officer_view/<group_id>')
def ring_officer_view(group_id):
    db=Db()
    res=db.select("SELECT * FROM department,officer,allocate_officer WHERE department.dept_id = allocate_officer.department_id AND allocate_officer.officer_id = officer.officer_id")
    return render_template('Admin/ring_officer_view.html',data=res,id=group_id)

@app.route('/ring_minister_view/<group_id>')
def ring_minister_view(group_id):
    db=Db()
    res=db.select("select * from department,minister,allocate_minister where department.dept_id = allocate_minister.dept_id and allocate_minister.minister_id = minister.minister_id")
    return render_template('Admin/ring_minister_view.html',data=res,id=group_id)

@app.route('/minister_add_ring/<g_id>/<m_id>')
def minister_add_ring(g_id,m_id):
    db=Db()
    ss=db.selectOne("select * from group_members where group_id='"+str(g_id)+"'and user_id = '"+str(m_id)+"'")
    if ss is not None:
        return '''<script>alert("already added"); window.location="/group_view"</script>'''
    else:
        db.insert("insert into group_members values ('','"+str(g_id)+"','"+str(m_id)+"') ")
        return '''<script>alert("minister added to ring ");window.location="/group_view"</script>'''

@app.route('/officer_add_ring/<g_id>/<o_id>')
def officer_add_ring(g_id,o_id):
    db=Db()
    ss= db.selectOne("select * from group_members where group_id='"+str(g_id)+"'and user_id='"+str(o_id)+"'")
    if ss is not None:
        return '''<script>alert("already added"); window.location="/group_view"</script>'''
    else:
        db.insert("insert into group_members values ('','"+str(g_id)+"','"+str(o_id)+"')")
        return'''<script>alert("officer added to ring");window.location="/group_view"</script>'''

# ------Minister------
@app.route('/minister')
def minister_home():
    if session['lg'] == "lin":
        return render_template('minister/index.html')
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
           db.insert("insert into suggestions VALUES('','"+str(session['m_id'])+"',curdate(),'"+res+"','pending','pending') ")
           return '''<script>alert("suggestion sent");window.location = "/minister_send_suggestions"</script>'''
        return render_template('minister/minister_send_suggestions.html')
    else:
        return redirect('/')

@app.route('/minister_chat')
def minister_chat():
    if session['lg'] == "lin":

        return render_template('minister/minister_chat.html')
    else:
        return redirect('/')

@app.route('/minister_chat1', methods=['post'])
def minister_chat1():

        db = Db()
        a = session['m_id']
        print(a)
        q1 = "SELECT *  FROM officer,allocate_minister,allocate_officer where allocate_minister.dept_id = allocate_officer.department_id and officer.officer_id = allocate_officer.officer_id and allocate_minister.minister_id = '"+str(session['m_id'])+"'"
        res = db.select(q1)
        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        print(rw)
        return rw

@app.route('/minister_send', methods=['post'])
def minister_send():

        db = Db()
        c = session['m_id']
        b = request.form['n']
        print(b)
        m = request.form['m']

        q2 = "insert into chat values(null,'" + str(c) + "','" + str(b) + "','" + m + "',now())"
        res = db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r

@app.route('/minister_reply', methods=['post'])
def minister_reply():

        print("...........................")
        c = session['m_id']
        b = request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id'] = c
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        return rw
#---------------Officer----------------

@app.route('/officer')
def officer_home():
    if session['lg'] == "lin":
        return render_template('officer/index.html')
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

@app.route('/officer_chat')
def officer_chat():
    if session['lg'] == "lin":
        return render_template('officer/officer_chat.html')
    else:
        return redirect('/')



@app.route('/officer_chat1',methods=['post'])
def officer_chat1():

        db=Db()
        a=session['o_id']
        print(a)
        q1="SELECT * FROM allocate_minister, allocate_officer,minister WHERE allocate_minister.minister_id = minister.minister_id and allocate_officer.department_id = allocate_minister.dept_id AND officer_id = '"+str(session['o_id'])+"'"
        res = db.select(q1)
        v={}
        if len(res)>0:
            v["status"]="ok"
            v['data']=res
        else:
            v["status"]="error"

        rw=demjson.encode(v)
        print(rw)
        return rw

@app.route('/officer_send',methods=['post'])
def officer_send():

        db=Db()
        c = session['o_id']
        b=request.form['n']
        print(b)
        m=request.form['m']

        q2="insert into chat values(null,'"+str(c)+"','"+str(b)+"','"+m+"',now())"
        res=db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r


@app.route('/officer_reply',methods=['post'])
def officer_reply():

        print("...........................")
        c = session['o_id']
        b=request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id']=c
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        return rw

@app.route("/upload")
def upload():
    return render_template("officer/upload.html")













# /============================================================

@app.route("/usr_doc_up1")
def usr_doc_up1():
    return render_template("officer/importent_document_to_minister.html")



@app.route("/usr_doc_up1_post",methods=['post'])
def usr_doc_up1_post():
    fl = request.files['fileField']
    alg=request.form['algo']
    # print(fl.filename)
    f_path = staticpath+"files\\" + fl.filename
    fl.save(f_path)
    enc_pth = staticpath + "encrypted\\doc\\" + fl.filename
    if alg=="AES":
        pswd=str(random.randint(0000,9999))
        bufferSize = 64 * 1024
        pyAesCrypt.encryptFile(f_path, enc_pth+".aes", pswd, bufferSize)
        # pyAesCrypt.decryptFile(enc_pth,"D:\\aaaa.docx",pswd,bufferSize)
        db=Db()
        qry="insert into document(path,algthm,allocate_officer_id,date,key_1) values('"+fl.filename+".aes','"+alg+"','"+str(session['o_id'])+"',CURDATE(),'"+pswd+"')"
        db.insert(qry)
        np.os.remove(f_path)
        return "ok"
    elif alg=="DES":
        from asw_file import file_des
        d_key = str(random.randint(10000000, 99999999)).encode('utf-8')
        key0 = DesKey(d_key)
        fd=file_des()
        enc_path=fd.des_encrypt(f_path,key0)
        key=d_key.decode('utf-8')
        qry = "insert into document(path,algthm,allocate_officer_id,date,key_1) values('" + enc_path + "','" + alg + "','" + str(session['o_id']) + "',CURDATE(),'" + key + "')"
        db=Db()
        db.insert(qry)
        np.os.remove(f_path)
        return "ok"








if __name__ == '__main__':
    app.run(port=4000)

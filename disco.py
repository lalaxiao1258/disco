# coding=utf-8
import invite,os
from  flask import Flask,jsonify,request
app = Flask(__name__)
@app.route("/disco/<invitecode>",methods=["GET"])
def disco(invitecode):
    a=invite.write_code(invitecode)
    if a:
        return jsonify({'code' :200, 'msg': '已提交！请勿重复提交！'})
    else:
        return jsonify({'code': 404, 'msg': '提交错误！'})
@app.route("/disco1/<invitecode>",methods=["GET"])
def disco1(invitecode):
    if len(invitecode)==12:
        
        f=open('invite1.txt','a')
        a=f.write(invitecode+'\n')
        f.close
        if a:
            return jsonify({'code' :200, 'msg': '已提交！请勿重复提交！'})
    else:
        return jsonify({'code': 404, 'msg': '提交错误！'})
             
@app.route('/invite1/delete',methods=["GET"])
def delete_code1():
    f=open('invite1.txt','w')
    a=f.write('')
    f.close() 
    if a:
        return jsonify({'msg':'True'})
    else:
        return jsonify({'msg':'False'}) 
@app.route('/invite1',methods=["GET"])
def invite1():
    with open('invite1.txt','r') as f:
    @app.route('/invite/delete',methods=["GET"])
def delete_code():
    a=invite.delete_code()
    if a:
        return jsonify({'msg':'True'})
    else:
        return jsonify({'msg':'False'})
@app.route("/invite_log",methods=["GET"])
def disco_log():
    log=open('111.txt','r')
    return log.read()
@app.route("/log",methods=["GET"])
def log():
        log = open('logg.log', 'r')
        return log.read()
@app.route("/invite",methods=["GET"])
def invitelog():
    log = open('invite.txt', 'r')
    return log.read()
@app.route('/invite/<num>',methods=['GET'])
def mun(num):
    if invite.code_num(num):
        return jsonify({'msg':'true','num':num})
    else:
        return jsonify({'msg':'false'})
@app.route("/log1",methods=["GET"])
def logg():
        log = open('log1.log', 'r')
        return log.read()
@app.route("/log2",methods=["GET"])
def log2():
        log = open('log2.log', 'r')
        return log.read()
if __name__ == '__main__':
    app.run(host='10.170.0.8',port=5000, debug=True)

            

                                     

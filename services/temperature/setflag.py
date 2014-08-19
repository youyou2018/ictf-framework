# -*- coding: utf-8 -*-
import socket
import cPickle
import base64
import marshal
import random
import time
import datetime
import pexpect

class SetFlag():

  def execute(self,ip,port,flag):

    def set_flag(server_socket):
      data = clientsock.recv(BUFSIZ)
      globals()["flag_id"] = int(data.split(",")[0])
      globals()["cookie"] = data.split(",")[1]
      globals()["flag"] = data.split(",")[2]
    
    error = -1
    error_msg = ''
    flag_id = datetime.datetime.fromtimestamp(random.randint(1,int(time.time()))).strftime("%Y/%m/%d")

    cookie = cities[random.randint(0,len(cities)-1)]

    try:
      s = socket.socket()
      s.connect((ip,port))

      msg = s.recv(1024)
      s.send("2")
      msg = s.recv(1024)
      if msg.startswith("Insert a date"):
	s.send(flag_id)
	msg = s.recv(1024)
	if msg.startswith("Insert a location"):
	  s.send(cookie)
	  msg = s.recv(1024)
	  if msg.startswith("Insert the recorded temperature:"):
	    s.send(flag)

      msg = s.recv(1024)
      error = 0

    except Exception as e:
      error = 42
      error_msg = str(e)

    self.flag_id = flag_id
    self.cookie = cookie
    self.error = error
    self.error_msg = error_msg
  
  def result(self):
    return {'FLAG_ID' : self.flag_id,
	    'TOKEN' : self.cookie,
	    'ERROR' : self.error,
	    'ERROR_MSG' : self.error_msg,
	    }
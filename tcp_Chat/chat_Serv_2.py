# -*-coding:utf-8-*-
__author__ = 'VeyronRomeo',
__author_email__ = 'killni.ma@163.com',
__time__ = '2017\11\6 0006 11:15 '
project = 'chat for TCP Intent Message'
"""
description=this is a  Intent message 1 to 1 chat room 
"""

from socket import *
from time import ctime
import select
import sys
import Queue

HOST = ''
PORT = 21566
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setblocking(False)  # 阻塞关闭

tcpSerSock.bind(ADDR)  # 绑定端口
tcpSerSock.listen(5)  # 监听连接

inputs = [tcpSerSock]

outputs = []

message_queues = {}
'''
while True:
    print 'waiting for connection...'
    #tcpCliSock, addr = tcpSerSock.accept()
    #print '...connected from:', addr
    #inputs.append(tcpCliSock)  # 将服务套接字加入到input列表中
    while True:
        readyInput, readyOutput, readyException = select.select(inputs, outputs,
                                                                inputs)  # 从input中选择，轮流处理client的请求连接（tcpSerSock），client发送来的消息(tcpCliSock)，及服务器端的发送消息(stdin)
        for indata in readyInput:
            if indata is tcpSerSock:  # 处理client发送来的消息
                tcpCliSock, addr = tcpSerSock.accept()
                print '...connected from:', addr
                inputs.append(tcpCliSock)

                print data
                if data == '88':
                    inputs.remove(tcpCliSock)
                    break
            else:  # 处理服务器端的发送消息
                data = raw_input('>')
                if data == '88':
                    tcpCliSock.send('%s' % (data))
                    inputs.remove(tcpCliSock)
                    break
                tcpCliSock.send('[%s] %s' % (ctime(), data))
        if data == '88':
            break
    tcpCliSock.close()
tcpSerSock.close()
'''

while inputs:
    print '\nwaiting for the next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # Handle inputs
    for s in readable:
        if s is tcpSerSock:
            # A "readable" server socker is ready to accpet a connection
            connection, client_addr = s.accept()
            print 'new connection from ', client_addr
            connection.setblocking(False)
            inputs.append(connection)

            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()

        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print (sys.stderr, '[%s] received "%s" from %s ' % (ctime(), data, s.getpeername()))
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                print ('closing', client_addr, 'after reading no data')
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)  # 客户端断开了，不用再给它返回数据了，所以这个时候移走客户端的连接
                inputs.remove(s)
                s.close()

                # remove message queue
                del message_queues[s]
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            # No message waiting so stop checking for writability
            print 'output queue for ', s.getpeername(), 'is empty'
            outputs.remove(s)
        else:
            print '[%s] sending "%s" to %s' % (ctime(),next_msg,s.getpeername())
            s.send(next_msg)
    for s in exceptional:
        print 'handling exceptional condition for ', s.getpeername()
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]

'''
while inputs:
    print '\nwaiting for the next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # Handle inputs
    for s in readable:
        if s is tcpSerSock:
            # A "readable" server socker is ready to accpet a connection
            connection, client_addr = s.accept()
            print 'new connection from ', client_addr
            connection.setblocking(False)
            inputs.append(connection)
        else:
            data = s.recv(1024)
            if data:
                print ('received "%s" from %s ' % (data, s.getpeername()))
                connection.send('your send %s' % (data))
                break
            else:
                data = data = raw_input('>')
                tcpSerSock.send('[%s] %s' % (ctime(), data))
'''

import socket, sys
from _thread import start_new_thread


try:
    listening_port = int(input("Enter Listening Port:"))
except KeyboardInterrupt as error:
    print("User Requested As Interrupt!")
    print("Application Exiting!")
    sys.exit(0)

max_conn = 5
buffer_size = 4096


def start():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', listening_port))
        sock.listen(max_conn)
        print("[*] Initializing Sockets ... Done")
        print("[*] Sockets Binded Successfully")
        print("[*] Server Started Successfully [ %d ]\n" % listening_port)
    except Exception as e:
        print("[*] Unable To Initialize Socket")
        sys.exit(2)

    while 1:
        try:
            conn, addr = sock.accept()
            data = conn.recv(buffer_size)
            start_new_thread(conn_string, (conn, data, addr))
        except KeyboardInterrupt:
            sock.close()
            print("[*] Proxy Server Shutting Down ...")
            sys.exit(1)
    sock.close()


def conn_string(conn, data, addr):
    try:
        first_line = data.split('\n')[0]
        print(first_line)
        url = first_line.split(' ')[1]
        http_pos = url.find("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos+3):]
        port_pos = temp.find("/")
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)
        webserver= ""
        port = -1
        if port_pos == -1 or webserver_pos < port_pos:
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]
            print(str(webserver)+":"+str(port))
        proxy_server(webserver, port, conn, data, addr)
    except Exception as e:
        pass


def proxy_server(webserver, port, conn, data, addr):
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(data)
        while 1:
            reply = s.recv(buffer_size)
            if len(reply) > 0:
                conn.send(reply)
                dar = float(len(reply))
                dar = float(dar / 1024)
                dar = "%.3s" % (str(dar))
                dar = "%s KB" % (dar)
                print("[*] Request Done: %s => %s <=" % (str(addr[0]), str(dar)))
            else:
                break
        s.close()
        conn.close()
    except socket.error as err:
        s.close()
        conn.close()
        sys.exit(1)

if __name__ == '__main__':
    start()

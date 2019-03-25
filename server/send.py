import socket, os, json, struct

IP = '127.0.0.1'
PORT = 8080
ADD = (IP, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADD)

# 上传文件
while True:
    file_path = input('请输入文件路径>>').strip()
    if not os.path.exists(file_path):
        print('文件不存在')
        continue
    file_name = (os.path.split(file_path))[1]
    f = open(file_path, 'rb')
    data = f.read()
    size = len(data)

    fileinfo_size = struct.calcsize("128sl")
    fhead = struct.pack('128sl'.encode(), os.path.basename(file_path).encode(), os.stat(file_path).st_size)
    client.send(fhead)
    while 1:
        if not data:
            print ('{0} file send over ...'.format(file_path) )
            break
        client.send(data)
    f.close()
    client.close()

    # hander = {
    #     'file_name': file_name,
    #     'length': size
    # }
    # # 报头序列化
    # hander_json = json.dumps(hander)
    # # 报头bytes转换
    # hander_bytes = hander_json.encode('utf-8')
    # # 报头长度固定
    # s_hander = struct.pack('i', len(hander_bytes))
    # # 传输报头长度
    # client.send(s_hander)
    # # 传输报头数据
    # client.send(hander_bytes)
    # # 传输文件数据
    # client.send(date.encode('utf-8'))

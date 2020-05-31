while True:
    s = input("请输入转换的公式:")
    s_shift=s.replace("^{'","'^{")
    s_shift = s_shift.replace("^{}","")
    print(s_shift)
# 坑爹 Typora 的latex 公式不能和Mathtype 有些不兼容 必须改变一点所以设置这个程序

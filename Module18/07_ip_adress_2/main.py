
def parse_ip(txt):
    ip_str = txt.split('.')
    ip = []
    if len(ip_str) != 4:
        print("Адрес — это четыре числа, разделённые точками.")
        return None
    for octet_str in ip_str:
        if len([c for c in octet_str if not c.isdigit()]) > 0:
            print(f"{octet_str} - это не целое положительное число")
            return None
        octet = int(octet_str)
        if octet > 255:
            print(f"{octet} превышает 255.")
            return None
        ip[len(ip):] = [octet]
    else:
        return ip

ip_str = input("Введите IP: ")
ip = parse_ip(ip_str)
if ip:
    print("IP-адрес {}.{}.{}.{} корректен.".format(*ip))

import math

def bin_to_int(bin):
    return math.floor(sum([math.pow(2,i) for i in range(len(bin)-1,-1,-1) if bin[len(bin)-1-i]=='1']))

def hex_to_bin(hex):
    bina=""
    h_b={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
         "A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    for bit in hex: 
        bina+=h_b[bit]
    return bina

def handle_packet_4(packet):
    has_next=True
    str_val=""
    while(has_next):
        if packet[0]=='0': has_next=False
        str_val+=packet[1:5]
        packet=packet[5:]
    return packet,bin_to_int(str_val)

def get_score(type,subs):
    if type=="000":
        return sum(subs)
    elif type=="001":
        score = 1
        for sub in subs: score*=sub
        return score
    elif type=="010":
        return min(subs)
    elif type=="011":
        return max(subs)
    elif type=="101":
        return subs[0] > subs[1]
    elif type=="110":
        return subs[0] < subs[1]
    elif type=="111":
        return subs[0] == subs[1]
    print("ERROR!")
    return 0,""

def handle_packet_X_0(packet,type):
    sub_packets_length=bin_to_int(packet[:15]) ; packet = packet[15:]
    sub_packets=packet[:sub_packets_length] ; packet = packet[sub_packets_length:]
    subs=[]
    while(len(sub_packets) > 0):
        sub_packets,score=identify_packet(sub_packets)
        subs.append(score)
    return packet,get_score(type,subs)

def handle_packet_X_1(packet,type):
    nb_of_direct_sub_packet=bin_to_int(packet[:11]) ; packet = packet[11:]
    subs=[]
    while(nb_of_direct_sub_packet > 0):
        nb_of_direct_sub_packet-=1
        packet,score = identify_packet(packet)
        subs.append(score)
    return packet,get_score(type,subs)

def identify_packet(packet):
    score=0
    if not "1" in packet : return 0
    packet = packet[3:] #remove version which was only used for part1
    type = packet[:3] ; packet = packet[3:]
    if type=="100": #ID4 -> literal number
        packet,to_add = handle_packet_4(packet)
        score+=to_add
    else:
        length_type_id=packet[0] ; packet = packet[1:]
        if length_type_id=="0":
            packet,to_add = handle_packet_X_0(packet,type)
            score+=to_add
        else:
            packet,to_add = handle_packet_X_1(packet,type)
            score+=to_add

    return packet,score

if __name__ == "__main__":
    f = open("AdventOfCode2021\\D16\\input.txt")
    input = f.read()
    f.close()
    master_pack = hex_to_bin(input)
    score = identify_packet(master_pack)[1]
    print(score)
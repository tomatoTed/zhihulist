import re


def cookie2dic(cookie_str):
    list=cookie_str.split(";",1)
    d={}
    for item in list:
        kv=item.split("=",1)
        d[kv[0]]=kv[1]
    return d


def is_phone(phone):
    return re.match("1\d{10}", str(phone)) is not None


def is_email(email):
    return re.match("\w+@\w+\.\w+", str(email)) is not None

def get_gender_name(gender_number):
    if gender_number==0:
        return "女"
    elif gender_number==1:
        return "男"
    else:
        return "未知"

if __name__ == "__main__":
    cookie="""_za=6ccb492d-61c6-406c-b0ab-eaede291acd2; udid="AAAAhxpdlAmPTvJoUWNdL6JucXfWqwL_We0=|1457762093"; d_c0="AIAAOShKoQmPTgLzU_o2tsquX8EObo2ehHU=|1458222789"; _zap=88f95666-2b7d-4a3d-9ba1-bb69e9c8b326; q_c1=0ec83509a6d144718069580212e58fff|1486212423000|1457355340000; aliyungf_tc=AQAAAGbxqi0V/AgA30W4brZkXVXsZ8a5; _xsrf=bb328b2fd79097f91fba79b6ec9886e9; l_cap_id="NTMwMWMxYTM0YWY5NDY2MzhjY2I2ZDk1ZjBhYThkNjM=|1488008689|50f467ba62c11580ff065cfd869aeac6d9c9d532"; cap_id="ODRkOWRjZmZkNzQ0NDg4MDlkMjBkMThiZWZlYTk3Njc=|1488008689|d553cdc002facf6b84cc43855be806706efcfeac"; __utmt=1; login="MTM4MDg0MzQ0ZGQyNDdlM2I3MzNlYjBkMDMxNWUzYmY=|1488008712|77f169f8984a0b201c7b605d519e1317c275929c"; nweb_qa=heifetz; __utma=51854390.602090100.1484485814.1486212425.1488008688.3; __utmb=51854390.10.8.1488008725531; __utmc=51854390; __utmz=51854390.1486212425.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-1|2=registration_date=20141018=1^3=entry_date=20141018=1; z_c0=Mi4wQUFCQUdMazZBQUFBZ0FBNUtFcWhDUmNBQUFCaEFsVk5DTVBZV0FCMUV1RS1wX2dNOUV5MTl1OHpmYnF2aXI0RzJB|1488008729|8d51f144847c2db391ada304788a8ba3adc6c04e"""
    #get_cookie_dic(cookie)
    print(is_phone(18200391582))
    print(is_email("18200391582@asdfsdfsdfasdf.com"))
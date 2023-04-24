'''
def check_correct(v_list: list):
    for i in v_list:
        if 'a' <= i <= 'z' or '0' <= i <= '9' or i in ('_', '.', '@'):
            continue
        else:
            flag = 1
            return flag
    flag = 0
    return flag
    
    
def check_email(v_email: str):
    if v_email.find('@') != -1 and v_email.find('.') != -1:
        v_part1, v_part2 = v_email.lower().split('@', 1)
        # áîëüøå îäíîãî ğàçà
        if len(v_part1) != 0 and len(v_part2) != 0:
            if check_correct(v_part1) or check_correct(v_part2):
                print('ÍÅÒ')
            else:
                print('ÄÀ')
        else:
            print('ÍÅÒ')
    else:
        print('ÍÅÒ')
    
    
check_email(input())
'''


# put your python code here
def check_mail(mail):
    allow = set("abcdefghijklmnopqrstuvwxyz0123456789_@.")
    nesessary = {"@", "."}
    print("ÄÀ") if nesessary <= mail <= allow else print("ÍÅÒ")


msg = set(input().lower())
check_mail(msg)
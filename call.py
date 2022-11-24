import sys
from pycall import CallFile, Call, Application, Context

def call(number, callerid, code, ANSWER_WAIT, ANSWER_DTMF_WAIT):
    
    vars = {
        "code": code, 
        "answer_wait": ANSWER_WAIT,
        "answer_dtmf_wait": ANSWER_DTMF_WAIT 
    }
    
    c = Call(
        'SIP/multifon-out/%s' % number, 
        callerid="%s" % callerid,
        variables=vars
    )
    con = Context('quit', 's', '1')
    cf = CallFile(c, con, user='asterisk')
    cf.spool()

if __name__ == '__main__':
    call(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
    )
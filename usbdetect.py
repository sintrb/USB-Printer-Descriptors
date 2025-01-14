# -*- coding: UTF-8 -*
'''
自动检测USB变动，并输出变动信息
'''
def main(argv):
    import os
    import time
    import datetime
    import argparse

    if argv == None:
        argv = sys.argv
    parser = argparse.ArgumentParser(prog=argv[0], add_help=True)
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        help="check interval in seconds",
        default=3,
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        help="the max check count, 0 means infinite",
        default=0,
    )
    args = parser.parse_args(argv[1:])


    _color_norm = "\033[0m"
    _color_del = "\033[31m"
    _color_add = "\033[32m"
    _color_over = "\033[34m"
    _color_end = "\033[0m"
    last = None
    count = 0
    while not args.count or count < args.count:
        cmd = 'lsusb'
        output = os.popen(cmd).read()
        curr = set(sorted([s.strip() for s in output.split('\n') if s.strip()]))
        if curr != last:
            if last is None:
                for d in curr:
                    print('%s%s%s' % (_color_norm, d, _color_end))
            else:
                adds = curr - last
                dels = last - curr
                print('%s%s%s' % (_color_over, datetime.datetime.now(), _color_end))
                for d in adds:
                    print(' %s+%s%s' % (_color_add, d, _color_end))
                for d in dels:
                    print(' %s-%s%s' % (_color_del, d, _color_end))
            last = curr
        time.sleep(3)

if __name__ == "__main__":
    import sys, io
    main(sys.argv)
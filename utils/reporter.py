import sys

class Reporter:
    def __init__(self,args):
        self.A = args.num1
        self.N = args.N
        self.op = args.op
        self.B = args.num2
        self.M = args.M
        self.r = args.r
        self.recording = dict()

    def create_recording(selfi,name):
        # [start_time, end_time,duration]
        self.recording[name] = [0] * 3

    def report(self):
        for name, recording in self.recording.items():
            print(f'task {anme}: {recording[-1]}s')


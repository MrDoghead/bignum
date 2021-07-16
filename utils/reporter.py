import sys

class Reporter:
    def __init__(self,desc,args):
        self.desc = desc
        self.A = args.num1
        self.op = args.op
        self.B = args.num2
        self.r = args.r
        self.ub = args.ub
        self.recording = dict()

    def create(self,name):
        self.recording[name] = 0

    def update(self,name,value):
        self.recording[name] += value

    def report(self):
        print(f'------ {self.desc} ------')
        for name, recording in self.recording.items():
            print(f'operation {name}: {recording} times')
        print('----------------------')


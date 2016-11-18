from captaincloud.task import field
from captaincloud.task import Task, TaskImpl

import subprocess
import threading


class RunLocalCommandImpl(TaskImpl):
    def run_thread(self, instream, outstream):
        data = instream.read(self.Input.buffer_size)
        while data:
            outstream.write(data)
            data = instream.read(self.Input.buffer_size)

    def run(self):
        Input = self.Input = self.task.Input
        Output = self.Output = self.task.Output
        args = [Input.executable] + Input.args
        self.process = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        t1 = threading.Thread(
            target=self.run_thread,
            args=[Input.stdin, self.process.stdin])
        t2 = threading.Thread(
            target=self.run_thread,
            args=[self.process.stdout, Output.stdout])
        t3 = threading.Thread(
            target=self.run_thread,
            args=[self.process.stderr, Output.stderr])
        t1.start(), t2.start(), t3.start()
        self.process.wait()
        t1.join(), t2.join(), t3.join()


class RunLocalCommand(Task):
    ID = 'cctasks.command.local.run'
    NAME = 'Run Local Command'
    impl = RunLocalCommandImpl

    class Input:
        executable = field.StringField()
        args = field.ListField(field.StringField(), default=[])
        stdin = field.ByteStreamField()
        buffer_size = field.IntegerField(default=256)

    class Output:
        stdout = field.ByteStreamField()
        stderr = field.ByteStreamField()

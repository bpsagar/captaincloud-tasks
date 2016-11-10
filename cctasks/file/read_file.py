from captaincloud.task import field
from captaincloud.task import Task, TaskImpl

import codecs
import six


class ReadTextFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        Output = self.task.Output
        with codecs.open(Input.filepath, encoding=Input.encoding) as fd:
            data = fd.read(self.task.Input.buffersize)
            while data:
                Output.stream.write(data)
                data = fd.read(self.task.Input.buffersize)
            fd.close()


class ReadTextFile(Task):
    ID = 'cctasks.file.text.read'
    NAME = 'Read Text File'
    impl = ReadTextFileImpl

    class Input:
        filepath = field.StringField()
        buffersize = field.IntegerField(default=102400)
        encoding = field.StringField(default=six.u('utf8'))

    class Output:
        stream = field.StringStreamField()


class ReadBinaryFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        Output = self.task.Output
        with open(Input.filepath, 'rb') as fd:
            data = fd.read(self.task.Input.buffersize)
            while data:
                Output.stream.write(data)
                data = fd.read(self.task.Input.buffersize)
            fd.close()


class ReadBinaryFile(Task):
    ID = 'cctasks.file.binary.read'
    NAME = 'Read Binary File'
    impl = ReadBinaryFileImpl

    class Input:
        filepath = field.StringField()
        buffersize = field.IntegerField(default=102400)

    class Output:
        stream = field.ByteStreamField()

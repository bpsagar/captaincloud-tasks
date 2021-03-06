from captaincloud.task import field
from captaincloud.task import Task, TaskImpl
from captaincloud.task.registry import TaskRegistry

import codecs
import six


class WriteTextFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        with codecs.open(Input.filepath, 'w', encoding=Input.encoding) as fd:
            data = Input.stream.read(self.task.Input.buffersize)
            while data:
                fd.write(data)
                data = Input.stream.read(self.task.Input.buffersize)
            fd.close()


@TaskRegistry.register
class WriteTextFile(Task):
    ID = 'cctasks.file.text.write'
    NAME = 'Write Text File'
    impl = WriteTextFileImpl

    class Input:
        filepath = field.StringField()
        buffersize = field.IntegerField(default=102400)
        encoding = field.StringField(default=six.u('utf8'))
        stream = field.StringStreamField()

    class Output:
        pass


class WriteBinaryFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        with open(Input.filepath, 'wb') as fd:
            data = Input.stream.read(self.task.Input.buffersize)
            while data:
                fd.write(data)
                data = Input.stream.read(self.task.Input.buffersize)
            fd.close()


@TaskRegistry.register
class WriteBinaryFile(Task):
    ID = 'cctasks.file.binary.write'
    NAME = 'Write Binary File'
    impl = WriteBinaryFileImpl

    class Input:
        filepath = field.StringField()
        buffersize = field.IntegerField(default=102400)
        stream = field.ByteStreamField()

    class Output:
        pass

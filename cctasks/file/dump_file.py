from captaincloud.task import field
from captaincloud.task import Task, TaskImpl
from captaincloud.task.registry import TaskRegistry

import codecs
import six


class DumpTextFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        with codecs.open(Input.filepath, 'w', encoding=Input.encoding) as fd:
            fd.write(Input.data)


@TaskRegistry.register
class DumpTextFile(Task):
    ID = 'cctasks.file.text.dump'
    NAME = 'Dump Text File'
    impl = DumpTextFileImpl

    class Input:
        filepath = field.StringField()
        encoding = field.StringField(default=six.u('utf8'))
        data = field.StringField()

    class Output:
        pass


class DumpBinaryFileImpl(TaskImpl):
    def run(self):
        Input = self.task.Input
        with open(Input.filepath, 'wb') as fd:
            fd.write(Input.data)


@TaskRegistry.register
class DumpBinaryFile(Task):
    ID = 'cctasks.file.binary.dump'
    NAME = 'Dump Binary File'
    impl = DumpBinaryFileImpl

    class Input:
        filepath = field.StringField()
        buffersize = field.IntegerField(default=102400)
        data = field.ByteField()

    class Output:
        pass

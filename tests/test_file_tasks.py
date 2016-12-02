from cctasks.file import (
    ReadBinaryFile, ReadTextFile, WriteBinaryFile, WriteTextFile,
    LoadBinaryFile, LoadTextFile, DumpBinaryFile, DumpTextFile
)

import os
import six
import unittest


class InMemoryStream(object):
    def read(self, n=-1):
        # if n == -1:
        #     n == len(self.buffer)
        result = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return result

    def write(self, data):
        self.buffer += data


class InMemoryStringStream(InMemoryStream):
    def __init__(self):
        self.buffer = six.u('')


class InMemoryByteStream(InMemoryStream):
    def __init__(self):
        self.buffer = six.b('')


class TestTextFile(unittest.TestCase):
    def test_read(self):
        with open('temp.txt', 'w') as fd:
            fd.write(six.u('Hello World'))
            fd.close()
        task = ReadTextFile(filepath=six.u('temp.txt'))
        stream = InMemoryStringStream()
        task.Output.stream.set_real_stream(stream)
        task.run()
        self.assertEqual(stream.buffer, six.u('Hello World'))

    def test_write(self):
        task = WriteTextFile(filepath=six.u('temp.txt'))
        stream = InMemoryStringStream()
        task.Input.stream.set_real_stream(stream)
        stream.write(six.u('Hello World'))
        task.run()
        self.assertEqual(six.u('Hello World'), open('temp.txt').read())

    def test_load(self):
        with open('temp.txt', 'w') as fd:
            fd.write(six.u('Hello World'))
            fd.close()
        task = LoadTextFile(filepath=six.u('temp.txt'))
        task.run()
        self.assertEqual(task.Output.data, six.u('Hello World'))

    def test_dump(self):
        task = DumpTextFile(filepath=six.u('temp.txt'))
        task.Input.data = six.u('Hello World')
        task.run()
        self.assertEqual(six.u('Hello World'), open('temp.txt').read())

    def tearDown(self):
        os.unlink('temp.txt')


class TestBinaryFile(unittest.TestCase):
    def test_read(self):
        with open('temp.txt', 'wb') as fd:
            fd.write(six.b('Hello World'))
            fd.close()
        task = ReadBinaryFile(filepath=six.u('temp.txt'))
        stream = InMemoryByteStream()
        task.Output.stream.set_real_stream(stream)
        task.run()
        self.assertEqual(stream.buffer, six.b('Hello World'))

    def test_write(self):
        task = WriteBinaryFile(filepath=six.u('temp.txt'))
        stream = InMemoryByteStream()
        task.Input.stream.set_real_stream(stream)
        stream.write(six.b('Hello World'))
        task.run()
        self.assertEqual(six.b('Hello World'), open('temp.txt', 'rb').read())

    def test_load(self):
        with open('temp.txt', 'wb') as fd:
            fd.write(six.b('Hello World'))
            fd.close()
        task = LoadBinaryFile(filepath=six.u('temp.txt'))
        task.run()
        self.assertEqual(task.Output.data, six.b('Hello World'))

    def test_dump(self):
        task = DumpBinaryFile(filepath=six.u('temp.txt'))
        task.Input.data = six.b('Hello World')
        task.run()
        self.assertEqual(six.b('Hello World'), open('temp.txt', 'rb').read())

    def tearDown(self):
        os.unlink('temp.txt')

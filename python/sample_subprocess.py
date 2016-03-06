#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import os
import subprocess
import logging
import signal
import random

#from eventlet import greenthread

LOG = logging

def _subprocess_setup():
    # Python installs a SIGPIPE handler by default. This is usually not what
    # non-Python subprocesses expect.
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)


def execute(*cmd, **kwargs):
    """Helper method to execute command with optional retry.

    If you add a run_as_root=True command, don't forget to add the
    corresponding filter to etc/nova/rootwrap.d !

    :param cmd:                Passed to subprocess.Popen.
    :param process_input:      Send to opened process.
    :param check_exit_code:    Single bool, int, or list of allowed exit
                               codes.  Defaults to [0].  Raise
                               exception.ProcessExecutionError unless
                               program exits with one of these code.
    :param delay_on_retry:     True | False. Defaults to True. If set to
                               True, wait a short amount of time
                               before retrying.
    :param attempts:           How many times to retry cmd.
    :param run_as_root:        True | False. Defaults to False. If set to True,
                               the command is run with rootwrap.

    :raises exception.NovaException: on receiving unknown arguments
    :raises exception.ProcessExecutionError:

    :returns: a tuple, (stdout, stderr) from the spawned process, or None if
             the command fails.
    """
    process_input = kwargs.pop('process_input', None)
    check_exit_code = kwargs.pop('check_exit_code', [0])
    ignore_exit_code = False
    if isinstance(check_exit_code, bool):
        ignore_exit_code = not check_exit_code
        check_exit_code = [0]
    elif isinstance(check_exit_code, int):
        check_exit_code = [check_exit_code]
    delay_on_retry = kwargs.pop('delay_on_retry', True)
    attempts = kwargs.pop('attempts', 1)
    run_as_root = kwargs.pop('run_as_root', False)
    shell = kwargs.pop('shell', False)

    if len(kwargs):
        raise Exception('Got unknown keyword args '
                        'to utils.execute: %r' % kwargs)

    if run_as_root and os.geteuid() != 0:
        cmd = ['sudo'] + list(cmd)

    cmd = map(str, cmd)

    while attempts > 0:
        attempts -= 1
        try:
            LOG.debug('Running cmd (subprocess): %s' % ' '.join(cmd))
            _PIPE = subprocess.PIPE  # pylint: disable=E1101

            if os.name == 'nt':
                preexec_fn = None
                close_fds = False
            else:
                preexec_fn = _subprocess_setup
                close_fds = True

            obj = subprocess.Popen(cmd,
                                   stdin=_PIPE,
                                   stdout=_PIPE,
                                   stderr=_PIPE,
                                   close_fds=close_fds,
                                   preexec_fn=preexec_fn,
                                   shell=shell)
            result = None
            if process_input is not None:
                result = obj.communicate(process_input)
            else:
                result = obj.communicate()
            obj.stdin.close()  # pylint: disable=E1101
            _returncode = obj.returncode  # pylint: disable=E1101
            LOG.debug('Result was %s' % _returncode)
            if not ignore_exit_code and _returncode not in check_exit_code:
                (stdout, stderr) = result
                raise Exception('Returncode is not in check_exit_code.')
            return result
        except Exception:
            if not attempts:
                raise
            else:
                LOG.debug('%r failed. Retrying.' % cmd)
                #if delay_on_retry:
                #    greenthread.sleep(random.randint(20, 200) / 100.0)
        finally:
            # NOTE(termie): this appears to be necessary to let the subprocess
            #               call clean something up in between calls, without
            #               it two execute calls in a row hangs the second one
            #greenthread.sleep(0)
            pass



class TestSubprocess(unittest.TestCase):
    def test_method(self):
        ret = execute('ls', '/')
        self.assertTrue(len(ret) > 0)

if __name__ == '__main__':
    unittest.main()


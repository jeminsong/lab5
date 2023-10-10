#!/usr/bin/env python3
#
# Copyright 2021-2023 Michael Shafae
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
""" Check student's submission; requires the main file and the
    template file from the original repository. """
# pexpect documentation
#  https://pexpect.readthedocs.io/en/stable/index.html

# ex.
# .action/solution_check_p1.py  part-1 asgt

import io
import logging
import math
import sys
import os
import re
import pexpect
from assessment import csv_solution_check_make
from logger import setup_logger

import lab_config as cfg

def regex_it(s):
    combine_white_space_regex = re.compile(r"\s+")
    s = combine_white_space_regex.sub(" ", s).strip()
    s = s.replace(' ', '\\s+').replace('\n', '\\s+')
    return f'\\s*{s}\\s*'

def run_p1(binary):
    """Run part-1"""
    logger = setup_logger()
    status = []
    error_values = ()
    values = (
                (0, 0, 0),
                (10, 10, 100),
                (123, 174, 21402),
                (26, 11, 286),
                (-4, 345, 0),
                (62, -24, 0),
                (-456, -34, 0),
            )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p1_error(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    
    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p1(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status

def _run_p1_error(binary, values):
    raise NotImplementedError

def _run_p1(binary, values):
    """The actual test with the expected input and output"""
    logger = setup_logger()
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer

    expected = f'{values[0]} x {values[1]} = {values[2]}'
    values = list(map(str, values))
    
    prompts = [
        'Enter the length of the rectangle: ',
        'Enter the width of the rectangle: ',
    ]
    
    for curr_prompt, response in zip(prompts, values):
        # i = 0
        regex_prompt = regex_it(curr_prompt)
        try:
            proc.expect(
                fr'(?i){regex_prompt}'
            )
        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
            expected_error = f'Expected: "{curr_prompt}"'
            logging.error(expected_error)
            logging.error('Could not find expected output.')
            logging.info("%s", str(exception))
            logging.debug(str(proc))
            return status

        # proc.sendline(values[i])
        # i += 1
        proc.sendline(response)

    regex_expected = regex_it(expected)
    try:
        proc.expect(
            fr'(?i){regex_expected}'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        expected_error = f'Expected: "{expected}"'
        logging.error(expected_error)
        logging.error('Could not find expected output.')
        logging.info("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status

def run_p2(binary):
    """Run part-2"""
    logger = setup_logger()
    status = []
    error_values = (
        (-2147483648.123, "The input is too small to convert to an integer. Exiting."),
        (-2147483647.9999999, "The input is too small to convert to an integer. Exiting."),
        (2147483646.99999999, "The input is too larger to convert to an integer. Exiting."),
        (2147483647.123, "The input is too larger to convert to an integer. Exiting."),
    )
    values = (
                (1.234, 1, 2, 6),
                (45.8745, 45, 10, 3),
                (2.298, 2, 3, 4),
                (1.592, 1, 7, 0),
                (6.93, 6, 11, 1),
                (-1.234, -1, 2, 6),
                (-45.8745, -45, 10, 3),
                (-2.298, -2, 3, 4),
                (-1.592, -1, 7, 0),
                (-6.93, -6, 11, 1),
            )
    for index, val in enumerate(error_values):
        test_number = index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p2_error(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    
    for index, val in enumerate(values):
        test_number = len(error_values) + index + 1
        logger.info('Test %d - %s', test_number, val)
        rv = _run_p2(binary, val)
        if not rv:
            logger.error("Did not receive expected response for test %d.", test_number)
        status.append(rv)
    return status

def _run_p2_error(binary, values):
    """The actual error test with the expected input and output"""
    logger = setup_logger()
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer

    expected = values[1]
    values = list(map(str, values))
    
    prompts = [
        'Enter the number of feet you wish to convert to feet-inch:',
    ]
    
    for curr_prompt, response in zip(prompts, values):
        regex_prompt = regex_it(curr_prompt)
        try:
            proc.expect(
                fr'(?i){regex_prompt}'
            )
        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
            expected_error = f'Expected: "{curr_prompt}"'
            logging.error(expected_error)
            logging.error('Could not find expected output.')
            logging.info("%s", str(exception))
            logging.debug(str(proc))
            return status

        proc.sendline(response)

    regex_expected = regex_it(expected)
    try:
        proc.expect(
            fr'(?i){regex_expected}'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        expected_error = f'Expected: "{expected}"'
        logging.error(expected_error)
        logging.error('Could not find expected output.')
        logging.info("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 1 or proc.exitstatus == 0:
        status = True
    return status
    
def _run_p2(binary, values):
    """The actual test with the expected input and output"""
    logger = setup_logger()
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer

    expected = f'{values[0]} feet is {values[1]} feet, {values[2]} and {values[3]}/8 inches'
    values = list(map(str, values))
    
    prompts = [
        'Enter the number of feet you wish to convert to feet-inch:',
    ]
    
    for curr_prompt, response in zip(prompts, values):
        regex_prompt = regex_it(curr_prompt)
        try:
            proc.expect(
                fr'(?i){regex_prompt}'
            )
        except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
            expected_error = f'Expected: "{curr_prompt}"'
            logging.error(expected_error)
            logging.error('Could not find expected output.')
            logging.info("%s", str(exception))
            logging.debug(str(proc))
            return status

        proc.sendline(response)

    regex_expected = regex_it(expected)
    try:
        proc.expect(
            fr'(?i){regex_expected}'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        expected_error = f'Expected: "{expected}"'
        logging.error(expected_error)
        logging.error('Could not find expected output.')
        logging.info("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status

if __name__ == '__main__':
    cwd = os.getcwd()
    repo_name = os.path.basename(cwd)
    td = sys.argv[1]

    if sys.argv[1] == 'part-1':
        part_config = cfg.lab['parts'][0]
        _program_name = part_config['target']
        _files = part_config['src'].split() + part_config['header'].split()
        _do_format_check = part_config['do_format_check']
        _do_lint_check = part_config['do_lint_check']
        _do_unit_tests = part_config['do_unit_tests']
        _tidy_options = part_config['tidy_opts']
        _skip_compile_cmd = part_config['skip_compile_cmd']
        # There needs to be some magic here to figure out which due date to use.
        _lab_due_date = cfg.lab['mon_duedate'].isoformat()
        _run_func = locals()[part_config['test_main']]
    elif sys.argv[1] == 'part-2':
        part_config = cfg.lab['parts'][1]
        _program_name = part_config['target']
        _files = part_config['src'].split() + part_config['header'].split()
        _do_format_check = part_config['do_format_check']
        _do_lint_check = part_config['do_lint_check']
        _do_unit_tests = part_config['do_unit_tests']
        _tidy_options = part_config['tidy_opts']
        _skip_compile_cmd = part_config['skip_compile_cmd']
        # There needs to be some magic here to figure out which due date to use.
        _lab_due_date = cfg.lab['mon_duedate'].isoformat()
        _run_func = locals()[part_config['test_main']]
    else:
        print(f'Error: {sys.argv[0]} no match.')
        sys.exit(1)
    # Execute the solution check
    csv_solution_check_make(
        csv_key=repo_name, target_directory=td, program_name=_program_name, run=_run_func, files=_files, do_format_check=_do_format_check, do_lint_check=_do_lint_check, do_unit_tests=_do_unit_tests, tidy_options=_tidy_options, skip_compile_cmd=_skip_compile_cmd, lab_due_date=_lab_due_date
    )

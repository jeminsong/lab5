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
import pexpect
from assessment import csv_solution_check_simple
from logger import setup_logger

def regex_it(s):
    s = s.replace(' ', '\\s+').replace('\n', '\\s+')
    return f'\\s*{s}\\s*'

def run_p1(binary):
    """Run part-1"""
    logger = setup_logger()
    status = []
    error_values = ()
    values = (
                # Pepz
                (12, 18.50, 0.163576),
                (18, 26.50, 0.104138),
                # Mr Taco Nice
                (14, 16.99, 0.110369),
                # Pizza Hut
                (14, 13.99, 0.090881),
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
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer
    expected = values[-1]
    values = list(map(str, values))
    
    i = 0
    try:
        proc.expect(
            r'(?i)\s*Enter\s*pizza\s*diameter\s*in\s*inches:\s*'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter pizza diameter in inches:"')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        proc.expect(
            r'(?i)\s*Enter\s*pizza\s*price\s*in\s*dollars:\s*'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter pizza price in dollars:"')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        # Match and extract the floating point number
        regex = r'(?i)\s*Unit\s*price\s*=\s*([-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?)\s*dollars per square inch'
        match_index = proc.expect(regex)
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Unit price = %f dollars per square inch"', expected)
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    token = proc.match.group(1).decode("utf-8") 
    actual = float(token)
    # 1% tolerance
    if not math.isclose(expected, actual, rel_tol=.01): 
        logging.error('logic error: actual numeric output is %f, which is expected to be %f', actual, expected)
        return status

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status

# adapted from fall 2022 lab 07 part 1
def run_p2(binary):
    """Run part-2"""
    # status = True
    status = []
    values = (
                (1, 1, 2022, 1, 1, 2023, 365),
                (1, 1, 1984, 1, 1, 1985, 366),
                (12, 25, 1275, 12, 25, 2522, 455457),
                (9, 21, 2022, 10, 31, 1980, -15300),
                (10, 1, 79, 9, 23, 2022, 709658),
            )
    for index, val in enumerate(values):
        logging.info('Test %d - %s', index + 1, val)
        # status = status and _run_p1(binary, val)
        rv = _run_p2(binary, val)
        if not rv:
            logging.error("Did not receive expected response for test %d.", index + 1)
        status.append(rv)
    return status

def _run_p2(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer
    values = list(map(str, values))
    
    i = 0
    try:
        proc.expect(
            r'(?i)\s*Enter\s*a\s*start\s*month:\s*'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter a start month: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        proc.expect(
            r'(?i)\s*Enter\s*a\s*start\s*day:\s*'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter a start day: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        proc.expect(
            r'(?i)\s*Enter\s*a\s*start\s*year:\s*'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter a start year: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1

    try:
        proc.expect(
            r'(?i)\s*Enter\s*an\s*end\s*month:\s*'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter an end month: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1
    
    try:
        proc.expect(
            r'(?i)\s*Enter\s*an\s*end\s*day:\s*'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter an end day: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1
    
    try:
        proc.expect(
            r'(?i)\s*Enter\s*an\s*end\s*year:\s*'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "Enter an end year: "')
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    proc.sendline(values[i])
    i += 1
    
    try:
        proc.expect(
            r'(?i)\s*The\s+number\s+of\s+days\s+between\s+{}/{}/{}\s+and\s+{}/{}/{}\s+is\s+{}\s+days\s*'.format(*values)
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Expected: "The number of days between {}/{}/{} and {}/{}/{} is {} days"'.format(*values))
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status
    
    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status

tidy_opts = (
    '-checks="*,-misc-unused-parameters,'
    '-modernize-use-trailing-return-type,-google-build-using-namespace,'
    '-cppcoreguidelines-avoid-magic-numbers,-readability-magic-numbers,'
    '-fuchsia-default-arguments-calls,-clang-analyzer-deadcode.DeadStores,'
    '-modernize-use-nodiscard,-modernize-pass-by-value,'
    '-bugprone-exception-escape,-llvm-header-guard"'
    ' -config="{CheckOptions: [{key: readability-identifier-naming.ClassCase, value: CamelCase}, '
    '{key: readability-identifier-naming.ClassMemberCase, value: lower_case}, '
    '{key: readability-identifier-naming.ConstexprVariableCase, value: CamelCase}, '
    '{key: readability-identifier-naming.ConstexprVariablePrefix, value: k}, '
    '{key: readability-identifier-naming.EnumCase, value: CamelCase}, '
    '{key: readability-identifier-naming.EnumConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.EnumConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.FunctionCase, value: CamelCase}, '
    '{key: readability-identifier-naming.GlobalConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.GlobalConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.StaticConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.StaticConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.StaticVariableCase, value: lower_case}, '
    '{key: readability-identifier-naming.MacroDefinitionCase, value: UPPER_CASE}, '
    '{key: readability-identifier-naming.MacroDefinitionIgnoredRegexp, value: \'^[A-Z]+(_[A-Z]+)*_$\'}, '
    '{key: readability-identifier-naming.MemberCase, value: lower_case}, '
    '{key: readability-identifier-naming.PrivateMemberSuffix, value: _}, '
    '{key: readability-identifier-naming.PublicMemberSuffix, value: \'\'}, '
    '{key: readability-identifier-naming.NamespaceCase, value: lower_case}, '
    '{key: readability-identifier-naming.ParameterCase, value: lower_case}, '
    '{key: readability-identifier-naming.TypeAliasCase, value: CamelCase}, '
    '{key: readability-identifier-naming.TypedefCase, value: CamelCase}, '
    '{key: readability-identifier-naming.VariableCase, value: lower_case}, '
    '{key: readability-identifier-naming.IgnoreMainLikeFunctions, value: 1}]}"'
)

if __name__ == '__main__':
    cwd = os.getcwd()
    repo_name = os.path.basename(cwd)
    if repo_name == sys.argv[1]:
        # Running from Make, it's changed directories
        td = '.'
    else:
        # Running as a workflow, it's at the root
        td = sys.argv[1]
    if sys.argv[1] == 'part-1':
        csv_solution_check_simple(
            csv_key=repo_name, target_directory=td, run=run_p1, files=['pizza.cc'], do_lint_check=False
        )
    if sys.argv[1] == 'part-2':
        csv_solution_check_simple(
            csv_key=repo_name, target_directory=td, run=run_p2, files=['datediff.cc'], do_lint_check=False
        )
    else:
        print(f'Error: {sys.argv[0]} no match.')

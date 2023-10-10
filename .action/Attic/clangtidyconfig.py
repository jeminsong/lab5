#!/usr/bin/env python3
"""Options for `clang_tidy` that work well for CPSC 120."""

# The list of disabled checks. (Note: all checks are enabled and then disabled, one by one.)
# List of clang tidy checks: https://clang.llvm.org/extra/clang-tidy/checks/list.html
checks = (
    '-checks="*,'
    '-misc-unused-parameters,'
    '-modernize-use-trailing-return-type,'
    '-google-build-using-namespace,'
    '-cppcoreguidelines-avoid-magic-numbers,'
    '-readability-magic-numbers,'
    '-fuchsia-default-arguments-calls,'
    # '-clang-analyzer-deadcode.DeadStores,'
    # '-bugprone-exception-escape,'
    # '-llvm-header-guard,'
    # '-cert-err58-cpp,'
    # '-fuchsia-statically-constructed-objects,'
    # '-cert-msc32-c,'
    # '-cert-msc51-cpp,'
    # '-google-runtime-references"'
    '"'
)

# Check options which conform to the Google C++ style guide, https://google.github.io/styleguide/cppguide.html.
# Clang documentation: https://clang.llvm.org/extra/clang-tidy/checks/readability/identifier-naming.html
check_options = (
    '-config="{CheckOptions: ['
    '{key: readability-identifier-naming.ClassCase, value: CamelCase}, '
    '{key: readability-identifier-naming.ClassMemberCase, value: lower_case}, '
    '{key: readability-identifier-naming.ConstexprVariableCase, value: CamelCase}, '
    '{key: readability-identifier-naming.ConstexprVariablePrefix, value: k}, '
    '{key: readability-identifier-naming.EnumCase, value: CamelCase}, '
    '{key: readability-identifier-naming.EnumConstantCase, value: CamelCase}, '
    '{key: readability-identifier-naming.EnumConstantPrefix, value: k}, '
    '{key: readability-identifier-naming.GlobalFunctionCase, value: CamelCase}, '
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
    '{key: readability-identifier-naming.IgnoreMainLikeFunctions, value: 1}'
    ']}"'
)

# Default compiler flags.
compiler_options = (
    '-std=c++17 -I /opt/local/include -I /usr/local/include'
)

def options_string():
    """Concatenate clang's checks and options into a single string ready to be used as a command line option."""
    return checks + ' ' + check_options

if __name__ == '__main__':
    # Just a demonstrate and test.
    import subprocess
    import sys
    if len(sys.argv) < 2:
        print('Provide an input C++ source file.')
        exit(1)
    cmd = 'clang-tidy'
    cmd = cmd + ' ' + options_string() + ' ' + sys.argv[1] + ' -- ' + compiler_options
    print(cmd)
    proc = subprocess.run(
        [cmd],
        capture_output=True,
        shell=True,
        timeout=120,
        check=False,
        text=True,
    )
    linter_warnings = str(proc.stdout).split('\n')
    linter_warnings = [line for line in linter_warnings if line != '']
    print('\n'.join(linter_warnings))

    
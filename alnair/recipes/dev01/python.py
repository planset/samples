# -*- coding: utf-8 -*-

from alnair import Package, Command

# If actual package name is different to "python",
# Package('actual package name') instead.
python = Package()

# Optional, please uncomment(remove leading '#') following lines and modify if
# necessary for package specific settings.
#
#python.setup.config('some config file path').contents("""\
#some config contents
#""")
#
# And you can also a host specific settings.
#with python.host('target host or IP address'):
#    python.setup.config('config file path').contents("""\
#configuration contents
#""")


# Optional, please uncomment(remove leading '#') following lines and modify if
# necessary for package specific setup command run after the installed.
#
#python.setup.after = Command(). \
#    run('something shell command'). \
#    sudo('shell command run under the root')

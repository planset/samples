#!/bin/bash

curl -L https://www.opscode.com/chef/install.sh | bash
/opt/chef/embedded/bin/gem install knife-solo --no-ri --no-rdoc



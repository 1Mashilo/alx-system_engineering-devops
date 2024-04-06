#!/usr/bin/pup

# This Puppet manifest defines a file resource for creating a file named 'school'
# in the '/tmp' directory with specific ownership, permissions, and content.

# Define a file resource
file { '/tmp/school':
  # Ensure the file exists
  ensure  => present,

  # Set owner to www-data user
  owner   => 'www-data',

  # Set group to www-data group
  group   => 'www-data',

  # Set file permissions (read, write, execute for owner, read for group)
  mode    => '0744',

  # Set content of the file
  content => 'I love Puppet',
}

package { 'nginx':
  ensure => installed,
}

file { '/data':
  ensure => directory,
}

file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  content => 'Holberton School',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
  require => File['/data/web_static/releases/test/index.html'],
}

exec { 'set_permissions':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => '/usr/bin',
  user    => 'root',
  group   => 'root',
}

file_line { 'nginx_alias_config':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'location /hbnb_static { alias /data/web_static/current/; }',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/data/web_static/current'],
}

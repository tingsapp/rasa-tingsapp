module.exports = {
  apps: [
    {
      name: 'rasa',
      script: '/var/www/html/rasa-tingsapp/venv/bin/rasa',
      args: 'run --enable-api',
      interpreter: '/var/www/html/rasa-tingsapp/venv/bin/python',
      env: {
        NODE_ENV: 'production',
        PATH: '/var/www/html/rasa-tingsapp/venv/bin:$PATH',
        VIRTUAL_ENV: '/var/www/html/rasa-tingsapp/venv',
      },
    },
  ],
};

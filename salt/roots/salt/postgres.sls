postgresql:
  pkg:
    - installed
  service:
    - running

postgresql-pkgs:
  pkg.installed:
    - pkgs:
      - libpq-dev
      - postgresql-server-dev-9.1
      - postgresql-contrib
    - require:
      - pkg: postgresql

template1-hstore:
  cmd.run:
    - name: sudo su -c 'psql -d template1 -c "CREATE EXTENSION IF NOT EXISTS hstore;"' postgres > /dev/null
    - shell: /bin/bash
    - require:
      - pkg: postgresql-pkgs

/etc/postgresql/9.1/main/postgresql.conf:
  file.append:
    - text: "listen_addresses = 'localhost'"
    - require:
      - pkg: postgresql-pkgs

/etc/postgresql/9.1/main/pg_hba.conf:
  file:
    - managed
    - source: salt://postgres/pg_hba.conf
    - require:
      - pkg: postgresql-pkgs

exposure-user:
  postgres_user.present:
    - name: exposure
    - password: exposure
    - runas: postgres
    - superuser: True
    - require:
      - cmd: template1-hstore

exposure-db:
  postgres_database.present:
    - name: exposure
    - owner: exposure
    - runas: postgres
    - require:
      - postgres_user: exposure-user
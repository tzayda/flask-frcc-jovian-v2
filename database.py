from sqlalchemy import create_engine, text

db_connection_string = 'mysql+pymysql://qdt5tsr34q66pnpb50dm:pscale_pw_AZ77Y976rmcVBg55mXsBIGbvhviPZLQVed6i8GlViko@aws.connect.psdb.cloud/flaskcareers?charset=utf8mb4'

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.mappings().all():
    result_dicts.append(dict(row))

  print(result_dicts)

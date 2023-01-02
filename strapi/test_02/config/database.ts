export default ({ env }) => ({
  connection: {
    client: 'postgres',
    connection: {
      host: env('DATABASE_HOST', 'rds-uc-terraform-dev-crawling-v1.cheuetgkxqpo.us-west-2.rds.amazonaws.com'),
      port: env.int('DATABASE_PORT', 5432),
      database: env('DATABASE_NAME', 'uct_crawling_v1'),
      user: env('DATABASE_USERNAME', 'uct_crawling_v1_root'),
      password: env('DATABASE_PASSWORD', 'ihvgXRxKbcZVCaPP'),
      ssl: env.bool('DATABASE_SSL', false),
    },
  },
});

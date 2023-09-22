"""changed nullable

Revision ID: e4d0d659b489
Revises: 4b97abcc4c27
Create Date: 2023-09-22 08:01:06.949487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4d0d659b489'
down_revision = '4b97abcc4c27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('Bakery_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('create_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=True)

    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.alter_column('create_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('create_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('create_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('Bakery_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('price',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###

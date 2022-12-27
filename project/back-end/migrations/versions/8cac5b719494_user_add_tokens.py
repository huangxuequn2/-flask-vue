"""user add tokens

Revision ID: 8cac5b719494
Revises: eb2612cc2023
Create Date: 2022-12-27 11:01:44.545552

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8cac5b719494'
down_revision = 'eb2612cc2023'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.String(length=32), nullable=True))
        batch_op.add_column(sa.Column('token_expiration', sa.DateTime(), nullable=True))
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
        batch_op.create_index(batch_op.f('ix_user_token'), ['token'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_token'))
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
        batch_op.drop_column('token_expiration')
        batch_op.drop_column('token')

    # ### end Alembic commands ###

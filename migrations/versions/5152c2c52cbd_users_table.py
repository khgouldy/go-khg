"""users table

Revision ID: 5152c2c52cbd
Revises: 4b7aea3b1a7a
Create Date: 2023-05-07 16:06:09.108821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5152c2c52cbd'
down_revision = '4b7aea3b1a7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('visits', sa.Integer(), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=120), nullable=False))
        batch_op.drop_column('visits')
        batch_op.drop_column('username')

    # ### end Alembic commands ###

"""empty message

Revision ID: 0b5f954c4f54
Revises: 506e478e0611
Create Date: 2019-06-03 19:07:02.662263

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0b5f954c4f54'
down_revision = '506e478e0611'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=False))
    op.alter_column('post', 'date_posted',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.alter_column('post', 'date_posted',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###

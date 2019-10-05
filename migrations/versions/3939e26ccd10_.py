"""empty message

Revision ID: 3939e26ccd10
Revises: 8a90acba4c19
Create Date: 2019-10-05 16:38:07.957255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3939e26ccd10'
down_revision = '8a90acba4c19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('login', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
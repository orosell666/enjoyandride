"""empty message

Revision ID: fb735a8972e0
Revises: 1be96ccd9e63
Create Date: 2022-03-25 19:29:41.798856

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fb735a8972e0'
down_revision = '1be96ccd9e63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthdate', sa.DateTime(), nullable=False))
    op.drop_column('user', 'fechanacimiento')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('fechanacimiento', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('user', 'birthdate')
    # ### end Alembic commands ###

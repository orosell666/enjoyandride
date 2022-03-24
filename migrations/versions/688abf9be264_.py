"""empty message

Revision ID: 688abf9be264
Revises: 2807edd385a2
Create Date: 2022-03-24 14:41:55.925149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '688abf9be264'
down_revision = '2807edd385a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('modelo', sa.String(length=120), nullable=False),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=120), nullable=False),
    sa.Column('tipo', sa.String(length=120), nullable=False),
    sa.Column('priceday', sa.Integer(), nullable=False),
    sa.Column('priceweek', sa.Integer(), nullable=False),
    sa.Column('discount1', sa.Integer(), nullable=False),
    sa.Column('discount2', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=300), nullable=False),
    sa.Column('provincia', sa.String(length=300), nullable=False),
    sa.Column('ciudad', sa.String(length=300), nullable=False),
    sa.Column('direccion', sa.String(length=300), nullable=False),
    sa.Column('latitud', sa.Integer(), nullable=False),
    sa.Column('longitud', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'latitud', 'longitud'),
    sa.UniqueConstraint('modelo')
    )
    op.add_column('user', sa.Column('lastName', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=80), nullable=False))
    op.create_unique_constraint(None, 'user', ['lastName'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'name')
    op.drop_column('user', 'lastName')
    op.drop_table('moto')
    # ### end Alembic commands ###
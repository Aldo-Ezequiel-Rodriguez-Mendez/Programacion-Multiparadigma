"""empty message

Revision ID: 3389cb5ae228
Revises: 
Create Date: 2022-10-31 09:42:13.653413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3389cb5ae228'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('empresa', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('director',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('escuela', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('empleado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('cargo', sa.String(length=250), nullable=True),
    sa.Column('departamento', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pasajero',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('companiavuelo', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profesor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('materia', sa.String(length=250), nullable=True),
    sa.Column('escuela', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profesor')
    op.drop_table('pasajero')
    op.drop_table('empleado')
    op.drop_table('director')
    op.drop_table('cliente')
    # ### end Alembic commands ###

"""empty message

Revision ID: c10feeba1c77
Revises: b756981a7d04
Create Date: 2022-04-01 09:24:08.040465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c10feeba1c77'
down_revision = 'b756981a7d04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('apellido', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('user_name', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('ciudad', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('estado', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('codigo_postal', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'codigo_postal')
    op.drop_column('user', 'estado')
    op.drop_column('user', 'ciudad')
    op.drop_column('user', 'user_name')
    op.drop_column('user', 'apellido')
    # ### end Alembic commands ###

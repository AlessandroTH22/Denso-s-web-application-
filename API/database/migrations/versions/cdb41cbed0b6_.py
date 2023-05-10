"""empty message

Revision ID: cdb41cbed0b6
Revises: b70a0cefad34
Create Date: 2022-04-20 10:18:05.791721

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cdb41cbed0b6'
down_revision = 'b70a0cefad34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('frogger')
    op.drop_table('flappy')
    op.drop_table('prueba')
    op.drop_table('instancia_prueba')
    op.drop_table('respuesta')
    op.drop_table('pregunta')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pregunta',
    sa.Column('id_pregunta', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('numPregunta', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('descripcion', mysql.VARCHAR(collation='utf8_unicode_ci', length=200), nullable=False),
    sa.Column('puntaje', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id_prueba', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_prueba'], ['prueba.id_prueba'], name='pregunta_ibfk_1'),
    sa.PrimaryKeyConstraint('id_pregunta'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('respuesta',
    sa.Column('id_respuesta', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('descripcion', mysql.VARCHAR(collation='utf8_unicode_ci', length=200), nullable=False),
    sa.Column('puntos', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id_instancia', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id_pregunta', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_instancia'], ['instancia_prueba.id_instancia'], name='respuesta_ibfk_1'),
    sa.ForeignKeyConstraint(['id_pregunta'], ['pregunta.id_pregunta'], name='respuesta_ibfk_2'),
    sa.PrimaryKeyConstraint('id_respuesta'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('instancia_prueba',
    sa.Column('id_instancia', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('fecha', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('puntajeTotal', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('nivelDesarrollo', mysql.VARCHAR(collation='utf8_unicode_ci', length=20), nullable=True),
    sa.Column('id_prueba', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], name='instancia_prueba_ibfk_2'),
    sa.ForeignKeyConstraint(['id_prueba'], ['prueba.id_prueba'], name='instancia_prueba_ibfk_1'),
    sa.PrimaryKeyConstraint('id_instancia'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('prueba',
    sa.Column('id_prueba', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(collation='utf8_unicode_ci', length=20), nullable=True),
    sa.PrimaryKeyConstraint('id_prueba'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('flappy',
    sa.Column('id_flappy', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('num_intentos', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('fecha_ultimoIntento', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('puntaje', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], name='flappy_ibfk_1'),
    sa.PrimaryKeyConstraint('id_flappy'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('frogger',
    sa.Column('id_frogger', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('num_intentos', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('num_nivel', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('fecha_ultimoIntento', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('puntaje', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], name='frogger_ibfk_1'),
    sa.PrimaryKeyConstraint('id_frogger'),
    mysql_collate='utf8_unicode_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
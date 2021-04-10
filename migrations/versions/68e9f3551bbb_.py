"""empty message

Revision ID: 68e9f3551bbb
Revises: 
Create Date: 2021-04-10 14:39:41.018992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68e9f3551bbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bootcamp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('generation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('bootcamp_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bootcamp_id'], ['bootcamp.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('generation')
    op.drop_table('bootcamp')
    # ### end Alembic commands ###
"""added_tips_table

Revision ID: 0187c3e840ee
Revises: 20cfeb1e8006
Create Date: 2023-04-12 01:34:14.134199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0187c3e840ee'
down_revision = '20cfeb1e8006'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('desc', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tips')
    # ### end Alembic commands ###
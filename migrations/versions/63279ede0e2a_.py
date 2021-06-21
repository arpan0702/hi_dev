"""empty message

Revision ID: 63279ede0e2a
Revises: f1259c8bbf97
Create Date: 2021-06-21 21:33:12.634991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63279ede0e2a'
down_revision = 'f1259c8bbf97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Company', sa.Column('date_updated', sa.Date(), nullable=True))
    op.add_column('Company', sa.Column('last_applied', sa.Date(), nullable=True))
    op.drop_column('Company', 'date_modified')
    op.drop_column('Company', 'applied')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Company', sa.Column('applied', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('Company', sa.Column('date_modified', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('Company', 'last_applied')
    op.drop_column('Company', 'date_updated')
    # ### end Alembic commands ###
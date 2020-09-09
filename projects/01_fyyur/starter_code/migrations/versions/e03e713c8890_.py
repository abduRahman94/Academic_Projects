"""empty message

Revision ID: e03e713c8890
Revises: 9838cf64dfe6
Create Date: 2020-08-13 21:03:41.471377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e03e713c8890'
down_revision = '9838cf64dfe6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venue_name', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shows', 'venue_name')
    # ### end Alembic commands ###

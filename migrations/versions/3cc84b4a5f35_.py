"""empty message

Revision ID: 3cc84b4a5f35
Revises: de8f6456fc6e
Create Date: 2023-05-11 12:43:18.225171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cc84b4a5f35'
down_revision = 'de8f6456fc6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appliance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(length=10), nullable=False))
        batch_op.add_column(sa.Column('value', sa.Float(), nullable=True))
        batch_op.drop_constraint('appliance_name_key', type_='unique')
        batch_op.drop_column('state')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appliance', schema=None) as batch_op:
        batch_op.add_column(sa.Column('state', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.create_unique_constraint('appliance_name_key', ['name'])
        batch_op.drop_column('value')
        batch_op.drop_column('type')

    # ### end Alembic commands ###
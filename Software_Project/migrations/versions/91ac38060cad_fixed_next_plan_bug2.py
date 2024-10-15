"""fixed Next plan bug2

Revision ID: 91ac38060cad
Revises: ef2f500f5709
Create Date: 2024-05-04 14:55:44.239079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91ac38060cad'
down_revision = 'ef2f500f5709'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('subscription_plan', schema=None) as batch_op:
        batch_op.alter_column('next_plan_id',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.drop_constraint('uq_stripe_price_id', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('subscription_plan', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_stripe_price_id', ['stripe_price_id'])
        batch_op.alter_column('next_plan_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###
